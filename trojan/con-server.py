import subprocess
import socketserver


class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024)
                print(self.data)
                print("{}send".format(self.client_address), self.data)

                rev = self.data.decode()
                rev = rev.rstrip()
                cmd = subprocess.Popen(rev, shell=True)

                if not self.data:
                    print("连接失败")
                    break
                self.request.sendall(self.data.upper())
        except Exception as e:
            print(self.client_address, '断开连接')
        finally:
            self.request.close()

    def setup(self):
        print("handle之前执行，建立连接", self.client_address)

    def finish(self):
        print("handle之后执行")


if __name__ == '__main__':
    host, port = '127.0.0.1', 5555
    server = socketserver.TCPServer((host, port), myserver)
    server.serve_forever()
