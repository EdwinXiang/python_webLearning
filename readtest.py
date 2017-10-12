#coding:utf-8
file = open('test.txt','r')
print file
#content = file.readlines()
for str in file:
	if str.startswith("#"):
		continue
	else:
		print str	
