
import socketserver


class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024)
                print(self.data.decode())

                # print("{}send".format(self.client_address), self.data)
                cmd = input("quit>>").strip()
                if len(cmd)==0:
                    continue
                if cmd == 'quit':
                    break
                if not self.data:
                    print("fail")
                    break

                self.request.sendall(cmd.encode())

        except Exception as e:
            print(self.client_address, '断开连接')
        finally:
            self.request.close()

    def setup(self):
        print("handle之前执行，建立连接", self.client_address)

    def finish(self):
        print("handle之后执行")


if __name__ == '__main__':
    host, port = '0.0.0.0', 9527
    server = socketserver.TCPServer((host, port), myserver)
    server.serve_forever()
