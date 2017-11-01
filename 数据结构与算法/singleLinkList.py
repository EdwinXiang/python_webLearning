#coding:utf-8

class SingleNode(object):
	"""docstring for SingleNode"""
	def __init__(self, item):
		self.item = item
		self.next = None


class SingleLinkList(object):
	"""单链表"""
	def __init__(self):
		self._head = None


	def is_empty(self):
		"""判断链表是否为空"""
		return self.__head == None


	def length(self):
		"""链表长度"""
		# cur 初始时指向头节点
		cur = self._head
		count = 0
		# 尾节点指向None，当为达到尾部时
		while cur != None:
			count += 1
			cur = cur.next
		return count


	def travel(self):
		"""遍历链表"""
		cur = self._head
		while cur !== None:
			print cur.item,
			cur = cur.next
		print ""


	def add(self,item):
		"""头部添加元素"""
		# 先创建一个保存item值的节点
		node = SingleNode(item)
		# 将新节点的链接域next纸箱头节点，即_head指向的位置
		node.next = self._head
		# 将链表的头_head指向新节点
		self._head = node


	def append(self,item):
		"""尾部添加元素"""
		node = SingleNode(item)
		# 先判断链表是否为空，若是空链表，则将_head指向新节点
		if self.is_empty():
			self._head = node
		#若不为空，则找到尾部，将尾节点的next指向新节点
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = None