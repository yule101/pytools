import argparse
import sys
import time
import requests
import colorama
from sqlalchemy import false

if sys.version_info < (3, 0):
    sys.stdout.write("需要python3以上环境。\n")
    sys.exit(1)

# 检测url的连接性，如果访问失败则不拼接字典，节省时间
def url_alive(url):
    a_url = []
    disa_url = []
    for u in url:
        try:
            print("正在检测{}连通性.....\r".format(u.strip()))
            requests.get(u, stream=True, verify=False, timeout=1)
            a_url.append(u)
        except requests.exceptions.ConnectionError:
            # print("http连接失败", e)
            disa_url.append(u.strip())
            continue
        except KeyboardInterrupt as e:
            print("用户中断.....")

    return a_url, disa_url


def dirscan(url, dic):
    # url = 'http://localhost/'
    t_start = time.time()  # 计算程序运行时间

    file = open('{}'.format(url), 'r', encoding='utf-8')  # 打开url文件
    dicc = open('{}'.format(dic), 'r', encoding='utf-8')  # 打开字典文件
    urllist = file.readlines()
    dicclsit = dicc.readlines()
    alive_url, disalive_url = url_alive(urllist)

    print("以下url访问失败：")
    for i in disalive_url:
        print(i)

    print("\n")
    for f in alive_url:  # 一行一行处理
        print("正在扫描{}".format(f.strip()))
        for d in dicclsit:
            payload = f.strip() + "/" + d.strip()  # 字典和url组合起来

            req = requests.get(payload, allow_redirects=false, stream=True, verify=False)  # get请求,302不跳转。

            # 根据状态码的不同，打印不同的颜色
            if req.headers.get("Content-Length"):
                if req.status_code == 200:
                    print(colorama.Fore.GREEN + "200  " + req.headers["Content-Length"] + "B  " + payload)
                if req.status_code == 302:
                    print(colorama.Fore.YELLOW + "302  " + req.headers.get("Content-Length") + "B  " + payload)
                if req.status_code == 400:
                    print(colorama.Fore.CYAN + "400  " + req.headers.get("Content-Length") + "B  " + payload)
                if req.status_code == 403:
                    print(colorama.Fore.RED + "403  " + req.headers.get("Content-Length") + "B  " + payload)
                if req.status_code == 500:
                    print(colorama.Fore.BLUE + "500  " + req.headers.get("Content-Length") + "B  " + payload)
            else:
                print(
                    colorama.Fore.GREEN + "200  " + "chunked  " + payload)  # 有些文件太大，会采取分块传输的方式，这个时候时没有content-length的。
        print("\n")

    t_end = time.time()
    print("运行时间：{}".format(t_end - t_start))


# 从命令接收url和file参数
def baner():
    parser = argparse.ArgumentParser(description="一个简单的目录扫描器", add_help=True)  # 在-h时显示的内容
    parser.add_argument("-uf", "--file", required=True)  # -u和--url都可以，参数必填
    parser.add_argument("-f", "--dic", default="dir.txt")  # 非必填，默认根目录下的dir.txt
    args = parser.parse_args()  # 获得一个对象
    dirscan(args.file, args.dic)


if __name__ == "__main__":
    baner()
