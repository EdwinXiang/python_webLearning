#coding:utf-8
# tcp服务器

from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET,SOCK_STREAM)

#绑定本地信息
adress = ('',7788)
tcpSerSocket.bind(adress)

#使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接受别人的链接啦
tcpSerSocket.listen(5)

# 如果有新的客户端来连接服务器，那么就产生一个新的套接字专门为这个客户端服务器
# newSocket用来为这个客户端服务
# tcpSerSocket就可以省下来专门等待其他新客户端的链接
newSocket,clientAddr = tcpSerSocket.accept()

# 接受对方发送过来的数据，最大接收1024个字节
recvData = newSocket.recv(1024)
print '接收到的数据为:',recvData

# 发送一些数据到客户端
newSocket.send("thank you!")

# 关闭为这个客户端服务的套接字，只要关闭了，就意味着不能再为这个客户端服务了，如果还需要服务，只能再次重新链接
newSocket.close()

#关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的链接
tcpSerSocket.close()