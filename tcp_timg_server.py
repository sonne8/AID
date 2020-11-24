"""
练习1：  从客户端上传一张图片给服务端，在服务端以
当前日期为名称存储。

比如： 客户端 将图片 timg.jpg 发送给服务端
      服务端存储为  2020-11-13.jpg 即可

思路 ： 客户端   打开文件 读取文件  发送文件
       服务端   打开文件 接收内容  写入文件
"""
from socket import *
import time

# 接收文件
def recv_image(connfd):
    filename="%d-%d-%d"%time.localtime()[:3]
    with open(filename,'wb')as f:
        while True:
            # 收发数据
            data = connfd.recv(1024)
            # 如果输入为空则结束
            if not data==b"##":
                break
            f.write(data)
    connfd.send("上传完成".encode())


def main():
    # 创建tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    # 绑定地址
    tcp_socket.bind(("0.0.0.0",8810))
    # 设置监听套接字
    tcp_socket.listen(5)
    # 循环等待处理客户端链接
    while True:
        print("Waiting for connect.....")
        connfd,addr=tcp_socket.accept()
        print("connect from",addr)
        recv_image(connfd)
        connfd.close()
# 关闭
    tcp_socket.close()

if __name__=='__main__':
    main()

