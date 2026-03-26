""""""
"""
匿名函数:就是没有名字的函数，不需要def关键字去定义
语法:lambda关键字来定义匿名函数，格式：lambda  参数:表达式
使用场景：当一个函数只使用一次，只做一点小事，推荐使用匿名函数
"""
def calculate(fu,a,b):
    print(f'计算结果为{fu(a,b)}')
calculate(lambda x,y:x+y,20,30)
calculate(lambda x,y:x+y,30,30)

#lambda只能写一行
#不可以写代码块
#冒号右边必须是表达式，而且只能有一个表达式
#执行结果自动作为返回值
res = lambda age:'成年' if age>=18 else '未成年'
print(res(18))
res = lambda num:num*2
print(res(10))