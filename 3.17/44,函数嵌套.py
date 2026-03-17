# def one(name,msg):
#         print(f'我是{name},我想说:')
#         two(msg)
#         print('我想说今天天气真好')
# def two(msg):
#         print('--------------------')
#         print(msg)
#         print('--------------------')
# one('信思智学','你好啊')

def test1():
    print('我进入函数1')
    test2()
    print('我离开了函数1')
def test2():
    print('我进入函数2')
    test3()
    print('我离开了函数2')
def test3():
    print('我进入函数3')
    print('我在执行函数3')
    print('我离开了函数3')
test1()

k = 0
def test4():
    global k
    k  +=1
    if k >=5:
        test6()
    else:
        print('1')
        test5()
        print('2')
def test5():
    if k>=5:
        test6()
    else:
        print('3')
        test4()
        print('4')
def test6():
    print('5')
test4()