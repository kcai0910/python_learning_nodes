""""""
"""
在不修改原函数的情况下对函数进行增强的工具
#装饰器是一种可调用的对象（通常为函数），接收一个函数作为参数，并且返回一个新的函数
"""
def say_hello(fn):
    def wrappper(a,b):
        print('欢迎计算')
        fn(a,b)
    return wrappper

def add(a,b):
    print(f'a+b的值为{a+b}')
# add(10,20)

add_pro = say_hello(add)
add_pro(10,20)