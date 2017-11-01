#coding:utf-8
import time
start_time = time.time()

# 两重循环
for a in range(0,1001):
	for b in range(0,1001):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print("a=%d,b=%d,c=%d"%(a,b,c))

end_time = time.time()
print("elapsed:%f"%(end_time-start_time))
print("finished!")