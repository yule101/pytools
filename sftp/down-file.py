import paramiko
import warnings

# 屏蔽告警信息
warnings.filterwarnings('ignore')

# 实例化sftp对象
client = paramiko.Transport('112.74.79.95',22)
client.connect(username='root',password='Ss117825')

#实例化sftp对象
sftp = paramiko.SFTPClient.from_transport(client)

#上传文件
sftp.get('/test.txt','./test111.txt')

client.close()
