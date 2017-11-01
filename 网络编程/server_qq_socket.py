#coding:utf-8
from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET,SOCK_STREAM)

#绑定本地信息
address = ('',7788)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接受别人的链接了
tcpSerSocket.listen(5)

while True:
	# 如果有新的客户端来链接服务器，那么久产生一个信心的套接字专门为这个客户端服务器
	# newSocket用来为这个客户端服务
	# tcpSerSocket 久可以省下来专门等待其他新客户端的链接

	newSocket,clientAddr = tcpSerSocket.accept()

	while True:
		# 接受对方发送过来的数据，最大的接受1024个字节
		recvData = newSocket.recv(1024)

		# 如果接受的数据的程度为0，则意味着客户端关闭了链接
		if len(recvData) > 0:
			print 'recv:',recvData
		else:
			break

		#发送一些数据到客户端
		sendData = raw_input("send:")
		newSocket.send(sendData)

	# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能在此链接
	newSocket.close()

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接受任何新的客户端的链接
tcpSerSocket.close()