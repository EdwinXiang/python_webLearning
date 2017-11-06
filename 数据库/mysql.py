#coding:utf-8
import MySQLdb

# try:
	conn = MySQLdb.connect(host='localhost',port=3306,db='stu',user='root',passwd='mysql',charset='utf8')
	cs1=conn.cursor()
	count=cs1.execute("insert into student(sname) values('zhangsan')")
	# print count
	conn.commit()
	cs1.close()
	conn.close()
# except Exception as e:
    # print e.message