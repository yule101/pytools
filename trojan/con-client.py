import socket

s = socket.socket()
s.connect(("127.0.0.1", 5555))
while True:
    cmd = input("quit退出>>").strip()
    if len(cmd) == 0:
        continue
    if cmd == 'quit':
        break
    s.send(cmd.encode())
    rev = s.recv(1024)
    print(rev.decode())
s.close()
