# !/usr/bin/env python
#coding:utf-8

import os

# 获取当前文件路径
path = os.getcwd()

fileList = os.listdir(path)


oldPrefix = raw_input("请输入要修改的文件前缀:")
newPrefix = raw_input("请输入修改后的文件前缀:")

def rename():
	for file in fileList:
	    print(file)
	    oldFile = os.path.join(path,file)
	    if os.path.isdir(oldFile):
		    continue
	    filename = os.path.splitext(file)[0]

	    if filename.find(oldPrefix) == -1:
	    	if filename == 'autoRename':
	    		pass
	    	else:
		    	newfile = newPrefix+filename
		    	newfileName = newfile + os.path.splitext(file)[1]
		    	os.rename(file,newfileName)
	    else:
		    newfile = filename.replace(oldPrefix,newPrefix)
		    newfileName = newfile + os.path.splitext(file)[1]
		    os.rename(file,newfileName)



if __name__ == '__main__':
	if not oldPrefix.strip():
	    print("修改的文件前缀不能为空")
	rename()
