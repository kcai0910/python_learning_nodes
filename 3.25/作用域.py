""""""
"""
什么是作用域？
作用域就是变量能够起作用的范围（变量可以在哪里使用，不可以在哪里使用）
全局作用域：整个.py文件最外层的范围，就是全局作用域
局部作用域：在函数内部范围，就是局部作用域
global: 把局部变量声明成全局变量
"""
#局部作用域和局部变量会在函数调用时创建，在函数执行完后自动销毁
def test():
    m=100
    m+=1
    print(f'我是函数中的m为{m}')
test()
test()
test()
#全局作用域和全局变量会在程序开始时创建，会在程序结束时销毁
m = 100
def test1():
    global m
    m+=1
    print(f'我是函数中的m为{m}')
test1()
print(m)
"""
函数嵌套:在函数执行的过程当中，调用了另外一个函数
"""
def one(name,msg):
    print(f'我叫{name},我想说{msg}')
    two(msg)
    print('one函数结束了')
def two(msg):
    print('************')
    print(msg)
    print('************')
one('xinsizhixue','python')