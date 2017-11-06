#coding:utf-8
import pymongo
# 链接客户端
client = pymongo.MongoClient('localhost',27017)
client.db
# 获得数据库runoob
db = client.runoob
# 获得集合
stu = db.stu

for cur in stu.find():
	print cur

# 获取文档个数
print stu.count()

# 添加文档
# s1 = {name:'gj',age:20}
# s1_id = stu.insert_one(s1).inserted_id

# 查找一个文档
# s2=stu.find_one()

# 查找多个文档
# for cur in stu.find():
	# print cur
