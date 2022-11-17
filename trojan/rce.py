import subprocess

cmd1 = subprocess.Popen(['ping', 'www.baidu.com'])
cmd2 = subprocess.Popen(['cmd.exe', '/c', 'dir'])

cmd1.wait()  # 要等待子进程结束，再执行下面，子进程就是cmd1和cmd2。
cmd2.wait()
print("主进程结束")