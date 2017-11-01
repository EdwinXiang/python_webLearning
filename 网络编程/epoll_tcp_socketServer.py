#coding:utf-8
import socket
import select

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置可以重复使用的绑定的信息
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定本级信息
s.bind(("",7788))

# 变为被动
s.listen(10)

# 创建一个epoll对象
epoll = select.epoll()

# 将创建的套接字添加到epoll的事件监听中
epoll.register(s.fileno(),select.EPOLLTN|select.EPOLLET)

connections = {}
addresses = {}

# 循环等待客户端的到来或者对方发送数据
while True:
	# epoll进行fd扫描的地方 -- 未制定超时时间则为阻塞等待
	epoll_list = epoll.poll()

	# 对事件进行判断
	for fd,events in epoll_list:
		# 如果socket创建的套接字被激活
		if fd == s.fileno():
			conn,addr = s.accept()

			print("有新的客户端到来%s"%str(addr))

			# 将conn和add信息分别保存起来
			connections[conn.fileno()] = conn
			addresses[conn.fileno()] = addr

			# 向epoll中注册链接socket的可读事件
			epoll.register(conn.fileno(),select.EPOLLTN | select.EPOLLET)

		elif events == select.EPOLLTN:
			# 从激活的fd上接收
			recvData = connections[fd].revc(1024)

			if len(recvData) > 0:
				print("recv:%s"%recvData)
			else:
				# 从epoll中移除该链接fd
				epoll.unregister(fd)

				# server侧主动关闭该链接fd
				connections[fd].close()

				print("%s---offline---"%str(addresses[fd]))