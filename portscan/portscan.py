import socket
import threading
import argparse


# 端口连接函数
def portscan(ip, p):
    global open_count  # 函数内修改全局变量，需要global
    try:
        # 建立socket连接
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, p))

        lock.acquire()  # 锁定，只能当前线程修改open_count
        open_count += 1
        print('{}   is open'.format(p))
        lock.release()  # 释放锁

        s.close()  # 关闭socket
    except:
        pass  # 如果端口不开放，就不打印信息


# 多线程函数
def multhread(arges):
    if 0 < arges.port < 65536:
        for p in range(arges.port):
            t = threading.Thread(target=portscan, args=(arges.ip, p))
            threads.append(t)
            t.start()
        for i in threads:
            i.join()  # 为了让所有的子线程执行完，再退出主线程
        print("扫描完成,{}个端口开放".format(open_count))
    else:
        print("端口超过范围！")


open_count = 0  # 存放开放多少端口
lock = threading.Lock()  # 锁是为了让多线程修改open_count的时候不会乱
threads = []  # 线程池


def help():
    parser = argparse.ArgumentParser(description="一个简单的端口扫描器", add_help=True)  # 在-h时显示的内容
    parser.add_argument("-i", "--ip", required=True)  # -i和--ip都可以，参数必填
    parser.add_argument("-p", "--port", type=int,required=False,default=65535)  # -i和--ip都可以，参数必填
    args = parser.parse_args()  # 获得一个对象
    multhread(args)


if __name__ == "__main__":
    help()
