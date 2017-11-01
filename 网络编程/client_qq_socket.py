#coding:utf-8
from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET,SOCK_STREAM)

# 链接服务器
serAddr = ('192.168.1.102',7788)
tcpClientSocket.connect(serAddr)

while True:
	# 提示用户输入数据
	sendData = raw_input("send:")

	if len(sendData) > 0:
		tcpClientSocket.send(sendData)
	else:
		break

	# 接收对方发送过来的数据,最大接收1024
	recvData = tcpClientSocket.recv(1024)
	print 'recv:',recvData

# 关闭套接字
tcpClientSocket.close()