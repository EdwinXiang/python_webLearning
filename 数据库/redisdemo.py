#coding:utf-8
import redis

try:
	r = redis.StrictRedis(host='localhost',port=6379)
	r.set('foo','bar')
	print(r.get('foo'))
except Exception as e:
	print e.message