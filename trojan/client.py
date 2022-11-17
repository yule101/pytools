import socket

msg = input("请输入需要执行的命令：")

s = socket.socket()
s.connect(('127.0.0.1',5555))

msg = msg.encode('gbk')

s.send(msg)

rev = s.recv(1024)
print(str(rev))
s.close()