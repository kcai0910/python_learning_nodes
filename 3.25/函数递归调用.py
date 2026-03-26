""""""
"""
递归调用：函数自己调用自己的 一种方式
"""
def hello(n):
    print(f'你好啊{n}')
    if n>1:
        hello(n-1)
    print(f'你好啊{n}')
hello(5)
#函数的说明文档
def add(a,b):
    """

    :param a:
    :param b:
    :return:
    """
add(10,20)