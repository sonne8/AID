"""
tcp_基础示例 客户端
"""
from socket import *
import time

ADDR = ("127.0.0.1", 8810)
filename=input("File:")

def mian():
    tcp_socket = socket()
    # 链接服务端
    tcp_socket.connect(ADDR)
    file=open(filename,'rb') #打开要上传的文件
    while True:
        data = file.read(1024)
        if not data:
            break
        # 数据收发
        tcp_socket.send(data)
    time.sleep(0.1) #防止粘包
    tcp_socket.send(b"##")  #传输结束
    data = tcp_socket.recv(1024)
    print(data.decode())

    tcp_socket.close()

if __name__=='__main__':
    mian()

