#coding:utf-8
class Queue(object):
	"""队列"""
	def __init__(self):
        self.items = []

    def is_empty(self):
    	return self.items == []

    def enqueue(self,item):
    	"""进队列"""
    	self.items.insert(0,item)

    def dequeue(self):
    	"""出队列"""
    	self.items.pop()

    def size(self):
    	return len(self.items)


if __name__ == '__main__':
	q = Queue()
	q.enqueue("hello")
	q.enqueue("world")
	q.enqueue("itcast")

	print q.size()
	print q.dequeue()
	print q.dequeue()
	print q.dequeue()