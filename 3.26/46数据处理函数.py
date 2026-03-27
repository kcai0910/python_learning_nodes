""""""
"""
reduce():将一组数据不断合并，最终合并成一个结果
#reduce(合并函数,可迭代对象，初始值)
"""
from functools import reduce
num = [1,2,3,4,5]
res = reduce(lambda x,y:x+y,num)
res2 = reduce(lambda x,y:x+y,num,100)
print(res)
print(res2)

# 合并字符串
str_list = ['python','java','web','js']
res3 = reduce(lambda a,b:a+b,str_list,'@@@@')
print(res3)
