""""""
"""
当一个函数的参数是函数,或者返回值是函数,那么该函数就是高阶函数
1:代码复用性高,可以把行为独立出去,传入不同的函数,实现不同的功能
2:函数更灵活,更通用
3:高阶函数是装饰器,闭包的基础
"""
#1 函数也是一个对象
a1 = 100 #a1是int的实例对象
a2 = 'hello' #a2是str类型的实例对象
a3 = [10,20,30] #a3是list类型的实例对象
def welcome():
    print('你好啊')
print(type(a1))
print(type(a2))
print(type(a3))
print(type(welcome)) #函数是function类类型的实例对象
#2 函数和对象一样可以添加属性
welcome.txt = '给函数添加一个属性'
welcome.version = 1.0
welcome()
print(welcome.version)
#3 函数可以赋值给变量
h = welcome
h()
print(h.txt)
#4 可变参数，不可变参数
#4.1不可变参数
# a = 100
# def add(num):
#     print(f'函数接受的num为{num},地址为{id(num)}')
#     num = 200
#     print(f'修改后的num为{num},地址为{id(num)}')
# print(f'我是函数调用后a,地址为{id(a)}')
# add(a)
# print(f'我是函数调用后{a},地址为{id(a)}')
# 4.2,可变参数
a = [10,20,30]
def add(num):
    print(f'函数接受的num为{num},地址为{id(num)}')
    num[0] = 50
    print(f'修改后的num为{num},地址为{id(num)}')
print(f'我是函数调用后{a},地址为{id(a)}')
add(a)
print(f'我是函数调用后{a},地址为{id(a)}')
#5 函数可以作为参数来使用
# def welcome():
#     print('你好啊')
# def say(f):
#     print('say函数开始调用')
#     f()
# say(welcome)
#6 函数可以作为返回值来使用
def welcome():
    print('你好啊99')
    def show(msg):
        print(msg)
    return show
res = welcome()
res('我是返回值函数')
print(res)
#7 函数可以有多个返回值
def calculate(x,y):
    res1 = x + y
    res2 = x - y
    return res1,res2
calculate(30,20)
a,b=calculate(30,20)
print('******')
print(a,b)

c,d = [10,20,100],'你好a'
print(c,d)

"""
当一个函数的参数是函数,或者返回值是函数,那么该函数就是高阶函数
1:代码复用性高,可以把行为独立出去,传入不同的函数,实现不同的功能
2:函数更灵活,更通用
3:高阶函数是装饰器,闭包的基础
"""
def info(msg):
    return '[提示:]'+msg
def warn(msg):
    return '[警告:]'+msg
def error(msg):
    return '[报错:]'+msg

def log(fun,txt):
    print(fun(txt))
log(info,'这是提示信息')
log(warn,'警告信息')
log(error,'报错信息')
