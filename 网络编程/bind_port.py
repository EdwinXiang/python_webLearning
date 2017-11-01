#coding:utf-8

from socket import *
# 绑定端口号

# 1、创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

# 2、绑定本地的相关嘻嘻，如果一个忘了程序不绑定，则系统会随机分配
bindAddr = ("",7788) # IP地址和端口号，IP一般不用写 表示本地的任何一个IP
udpSocket.bind(bindAddr)

# 3、等待接收方发送的数据
recvData = udpSocket.recvfrom(1024)

# 4、显示接收到的数据
print(recvData)

# 5、关闭套接字
udpSocket.close()