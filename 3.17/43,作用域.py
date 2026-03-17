#作用域就是变量能起作用的范围
"""

全局作用域：可以在任意一个位置被访问到
局部作用域：在函数内声名的变量，只能在函数内访问
global:可以声名变量为全局变量
"""

a = 100
def test():
    global a
    a = 300
    b = 200
    print(f'这是函数内部{a}')
    print(f'这是函数内部{b}')
print(a)
test()
# print(b) #会报错，因为变量b属于局部变量


c = 300
d = 400

def test2():
    e = '止血'
    f = '你好'
    global c
    c = 100
    print('函数内部打印c为',c)
    print('函数内部打印d为',d)
    print('函数内部打印e为',e)
    print('函数内部打印f为',f)
test2()
print('****************')
print('外部c为',c)
print('外部d为',d)
print('外部e为')
print('外部f为')
#局部变量在函数创建时调用，在函数执行完之后销毁
def test3():
    m = 100
    m+=1
    print(f'我函数内部{m}')
test3()
test3()
#全局变量，在程序开始时创建，在程序结束后销毁

def test4():
    global k
    k += 1
    print(f'我函数内部k{k}')
k = 100
test4()
test4()
test4()
test4()