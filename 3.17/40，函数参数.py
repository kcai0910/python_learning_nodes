#在使用位置参数的时候，实参和形参的顺序，数量要保持一致
def order(stu,num):
    print(f'{stu}班点了{num}份午餐')
order(2603,20)
order(20,2603)

#关键字参数
#关键字参数可以和位置参数混用，但是位置参数必须在关键字参数之前
def info(name,age,height,gender):
    print(f'我的名字是{name},我今年{age},我的身高{height},性别为{gender}')
info('guo~',18,178,'男')
info(name = 'guo~',gender = '男',age = 18,height = 178.5)
info('guo~',gender = '男',age = 18,height = 178.5)

#限制传参方式
#/：前面只能使用位置参数，*后面只能使用关键字参数
#/必须在*前面
def stu(name,/,height,*,age,gender):
    print(f'我的名字{name},我今年{age},我的身高是{height},性别为{gender}')
stu('数据',180,age = 18,gender='男')
#参数默认值
#如果调用函数传递参数，那么就是使用传入的值
#如果调用函数没有传递参数，那么就使用默认值
#注意如果某个形参设置了默认值，那么该形参后的所有参数，都需要设置默认参数
def stu2(name,height,age,gender,msg = '减肥'):
    print(f'我的名字{name},我今年{age},我的身高是{height},性别为{gender},我想说{msg}')
stu2('数据',180,age = 18,gender='男')
