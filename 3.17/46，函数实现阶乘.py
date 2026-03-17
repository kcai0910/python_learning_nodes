def test(n):
     """

    :param n:数字
    :return:阶乘
    """
def test(n):
    if n==0:
        return 1
    else :
        return n*test(n - 1)
res = fact(5)
print(res)


while True:
    res = input('请输入一段成绩')
# 函数计算7门学科的平均分，小于60不及格，大于60及格
