import paramiko
import warnings

# 屏蔽告警信息
warnings.filterwarnings('ignore')

# 实例化ssh对象
client = paramiko.SSHClient()
# 允许连接不在know_hosts文件的主机
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 连接
client.connect(hostname='127.0.0.1', port=22, username='root', password='xxxxx')

# 执行命令，返回三个值，标准输入，标准输出，错误句柄
stdin, stdout, stderr = client.exec_command('whoami')

# 读取标准输出
print(stdout.read())
