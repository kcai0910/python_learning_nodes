"""
递归调用:函数自己调用自己的一种操作
递归必须要具备终止条件(不能无限一直调用)
"""

#使用递归打印（从小到大）
def welcome1(n) :
    if n > 1:
        welcome(n-1)
    print(f'你好啊{n}')
#使用递归打印（从大到小）
def welcome2(n) :
    print(f'你好啊{n}')
    if n > 1:
        welcome(n-1)

welcome1(5)

def test(n,name):
    """
    这是test函数的注释
    :param n: 显示学生数量
    :param name: 显示学校名字
    :return: 返回一个结果
    """
test(10,'心血')
