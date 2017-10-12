#coding:utf-8
# 导入模块
import re

# 使用match方法进行匹配操作
result = re.match("^[0-9{11}$]","13240395822")
print(result.group())
