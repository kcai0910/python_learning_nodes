#1.局部作用域的生命周期
#每次调用函数的时候，会创建局部变量
#函数调用完成之后，局部变量会被销毁，变量会被释放
# def outer():
#     num = 10
#     num += 1
#     print(num)
# outer()
# outer()
# outer()
# 2：内部函数可以访问外部函数作用域的变量
# 访问外部变量是不需要nonlocal的，修改外部变量是需要的
#
# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num+=10
#         print(num)
#     inner()
# outer()

#闭包 内层函数+被内层使用的外层变量
# 1：函数必须嵌套
# 2:内层函数必须使用外层函数的变量
# 3：外层函数必须返回内层函数
def outer():
    num = 10
    msg = '心思自学'
    print(hex(id(num)))
    def inner():
        nonlocal num
        num+=1
        print(msg)
        print(num)
    return  inner
res= outer()
f=outer()
f()
f()
res()
print(res.__closure__)
print(res.__closure__[0].cell_contents)

#每次获得的闭包之间，互不影响（闭包之间是相互独立的）
#外层变量为可变对象时也是互不影响

#1:可以记住状态，不需要全局变量，实现变量私有化
#2：可以实现数据隐藏
#3：是装饰器的基础

# 缺点
#1：理解成本有点高，对新手不友好
#2：如果闭包里的变量得不到释放，会增加内存的占用