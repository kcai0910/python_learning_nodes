""""""
"""
作用域有四种 
Local :局部作用域 
Enclosing :外部函数作用域
Global ：全局作用域
Built-in ：内建作用域

查找顺序为LEGB

修改全局变量的值使用:global 变量
修改外部函数变量使用:nonlocal 变量                     
"""
#抛开全局就是内建作用域built-in
#全局作用域global
a = 100
#外部函数作用域enclosing
def test():
    print(f'我是test函数')
    global a
    b = 200
    c = 500
    a += 100
    print(f'我是test函数b为{b}')
    #内部函数作用域 local
    def inner():
        nonlocal c
        global a
        c +=100
        a+=100
        b=300
        print(f'我是inner函数b为{b}')
        print(f'我是inner函数a为{a}')
    inner()
    print(f'我是test函数c为{c}')
test()
print(f'我是全局a为{a}')
