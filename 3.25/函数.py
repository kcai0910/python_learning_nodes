""""""
"""
函数(function):可重复使用的，用于执行特定任务的代码
1，代码复用,减少重复代码
2,结构清晰,让程序更易读，方便开发人员维护
3，模块化开发，把功能拆分成若干个小功能，方便团队合作


#函数分为三大类
1:内置函数(print(),type(),range())
2，模块提供的函数，需要导入指定的模块才可以使用
3，自定义函数：就是开发人员自己定义的函数（先定义再使用）


def 函数名():
    函数体
函数名()

#形参:形式上的参数，用于接收实际的参数
#实参:实际的参数，是一个确切的值

形参只能在函数体里面使用
"""
def welcome():
    print('欢迎大家来到心思止血')
welcome()

def order(num,dish):
    print(f'你点了{num}份{dish}')
#位置参数 positional arguments
order(7,'桃花面')
order(2,'尖椒肉丝')

#函数参数
def info(name,age,gender,height):
    print(f'我是{name},我今年{age}岁,我是{gender}生,我的身高是{height}')
info('张强',18,'男','170')#positional arguments
info(height=170,name='家和',gender='男',age=21)#keyword argument关键字参数
#注意事项:当positional argument 和 keyword argments混用的时候，位置参数必须放在关键字参数之前
info('董小姐',18,height=175,gender='女')

#限制传参
#/前面只能写positional arguments *后面只能写keyword argument
#/ must be ahead of *
def infor(name,/,age,*,gender,height):
    print(f'我是{name},我今年刚满{age}岁,我是{gender}生，我的身高是{height}cm')
infor('果果',age=18,gender='男生',height=18)

#参数的默认值
#写在形参里的，如果有实参，就使用实参的值，如果没有实参，就走形参的默认值
def infor2(name,age,gender,height=170,msg=170):
    print(f'我是{name},我今年{age}岁,我是{gender}生，我的身高是{height}',{msg},)
infor2('赵卿',18,gender = '女')

# 可变位置参数 arguments
def test1(*args):
    print(args)
    print(type(args))
test1('张强',18,'男',170)

#可变关键字参数，实参一定是关键字参数
def  test2(**kwargs):
    print('test2')
    print(kwargs)
    print(type(kwargs))
test2(name = '啊涛',age=21,height=170)

def test3(a,b,*args,c='信思治学',**kwargs):
    print('test3')
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)
test3('张三','男','抽烟','喝酒','烫头',age = 21,height = 170)
