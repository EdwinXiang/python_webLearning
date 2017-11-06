#encoding=utf-8
import MySQLdb

try:
	conn = MySQLdb.connect(host='localhost',port=3306,db='stu',user='root',passwd='123',charset='utf8')
	cs1=conn.cursor()
	count=cs1.execute("insert into student(sname) values('zhangsan')")
	print(count)
	cs1.execute('select *from student')
	result=cs1.fetchall()
	print(result)
	# conn commit()
	cs1.close()
	conn.close()
except Exception as e:
	raise e