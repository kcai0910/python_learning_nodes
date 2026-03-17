#可变参数
def test1(*args):
    print(args)
    print(type(args))
    print(f'{args[0]},我今年{args[1]},我的身高{args[2]}')
test1('鹏翔',22,'175')
#可变关键字参数
#1:传递的实参是关键字实参，形参属于字典类型的数据
def test2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(f'我叫{kwargs['name']},我今年{kwargs['age']},我身高{kwargs['height']}')
test2(name='小姐',age=18,height=175)
#可变位置参数和可变关键字参数可以同时使用，但是必须先写可变位置参数
def test3(a,b,*args,c='心思',**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
test3('阿龙','男','抽烟','喝酒',height=175,age=18)


