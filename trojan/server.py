import subprocess
import socket

def command(cmd):
    cmd = subprocess.Popen(cmd,shell=True)
    return cmd
s = socket.socket()
s.bind(('127.0.0.1',5555))
s.listen()
msg = '欢迎光临'

while True:
    conn,addr = s.accept()
    print('来自{}的新连接......'.format(addr))
    conn.send(msg.encode('gbk'))
    rev = conn.recv(1024)
    data = bytes.decode(rev)
    print('命令是：'+data)
    output = command(data)
    conn.close()
