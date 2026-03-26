""""""
"""
None :是一个特殊的字面量，用来表示空值，无值，无意义
1:None 的类型是NoneType
2:None 出现在判断中会被当作False
3:None不可以参与数学运算，和字符串拼接
4:如果不给函数设置返回值，默认返回值为None
"""
a = None
print(type(None))
if a :
    print('可以进来')
# 函数执行的结果接受函数的返回值
res = print(1)
print(res)
"""
函数默认没有返回值，所以结果为None
我们可以通过return给函数设置返回值
1:return之后的代码，为当前函数的返回值
2:终止函数的运行,return后面的代码将不再运行
"""
