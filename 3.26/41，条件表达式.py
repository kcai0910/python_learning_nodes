""""""
"""
表达式：执行最后能得到一个值的代码，就是表达式
条件表达式:根据不同的条件得到不同的值，也被称为三元表达式，也叫三目运算
使用场景：二选一的情况
#值1（条件成立）判断 值2（条件不成立）
"""
#使用分支结构实现
age = 16
if age>=18:
    print('成年')
else :
    print('未成年')

#使用三元运算
res = '成年' if age>=18 else '未成年'
print(res)
isRain = True
# demo1
res2 = '点外卖'if isRain else '出去吃'
print(res2)
