#coding:utf-8
import re

urls = ["http://www.interoem.com/messageinfo.asp?id=35",
"http://3995503.com/class/class09/news_show.asp?id=14",
"http://3995503.com/class/class09/news_show.asp?id=14",
"http://lib.wzmc.edu.cn/news/onews.asp?id=769",
"http://www.zy-ls.com/alfx.asp?newsid=377&id=6",
"http://www.fincm.com/newslist.asp?id=415"
]
pattens = []
for string in urls:
	print(string)
	result = re.match("http:.*(com|cn)",string)
	# print(result.group())
	if result:
		pattens.append(result.group())
	else:
		print("error:匹配失败")



#匹配单词
danci = "hello world ha ha ha"
res = re.match(r"^[a-zA-Z]*\b",danci)
print(res.group()) 
print pattens