#None 是一个特殊的字面量，用来表示空值，无意义
s1 = ''
t1 = ()
msg = None
# 1,None的类型是NoneType
print(type(msg))
# 2:None转布尔值为False
print(bool(msg))
#3:可以参与判断，条件为假
if not msg:
    print('可以输出')
else :
    print('不可以 输出')
#4:不能参与运算
# print(msg+1)

#什么是返回值？
#函数执行完毕之后，会把执行结果交给调用着者，这个执行结果就是函数的返回值
res1 = type('你好啊')
res2 = int(15.6)
res3 = ord('a')
print(res1)
print(res2)
print(res3)

#对于自定义的函数，即便我们不设置返回值，函数也会默认返回None
#由于None 表示一个空值，那么也可以理解为这个函数没有返回值
def add(a,b):
    print(f'我接受的参数{a} ， {b}，两者相加为{a+b}')
    return '100'
    print('函数执行完毕')
sum = add(10,20)
print(sum)
#return之后的代码将不再执行
#return后面的值作为函数的返回值来使用

#print函数是没有返回值的
res4 = print('你好啊')
print(res4)

