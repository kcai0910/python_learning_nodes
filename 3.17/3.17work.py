# def ave(n):
#     res = int(input(f'第{n}个人的成绩:'))
#







"""
学生管理
功能 crud学生 菜单功能:
1:添加学生，
2 删除学生，
3查看所有学生
4录入成绩(可选)
5退出

"""
# dict1 = {}
# def stu(dict1):
#     print('\n=========学生管理系统==========')
#     print('请选择功能\n1:添加学生 2:删除学生 3:查看所有学生 4:录入成绩 5:退出')
#     res = int(input('请输入你的选择:'))
#     if res == 1:
#         stu1 = input('输入需要添加的学生姓名:')
#         dict1[stu1] = None
#         stu(dict1)
#     elif res == 2:
#         stu1 = input('请输入需要删除的学生姓名:')
#         if stu1 not in dict1:
#             print('学生不存在')
#         stu(dict1)
#     elif res == 3:
#         print(dict1.items())
#         stu(dict1)
#     elif res == 4:
#         stu1 = input('学生姓名:')
#         if stu1 in dict1:
#             cro = input(f'请输入{stu1}的成绩:')
#             dict1[stu1] = cro
#         else:
#             print('学生不存在')
#         stu(dict1)
#     elif res == 5:
#         return True;
#     else:
#         print('输入有误')
#         return False
#     return True
# if stu(dict1):
#     print('成功退出')


"""
def add():
        print('添加学生')
def main():
        print('这是菜单')
        choise = input('请输入你的操作:')
        if choise == 1:
        elif choise == 2:
        elif choise == 3:
        elif choise == 4:
        elif choise == 5:
        return break
while True
"""
dict1 = {}
def add():
    stu1 = input('学生姓名:')
    dict1[stu1] = None
def del1() :
    stu1 = input('请输入需要删除的学生姓名:')
    if stu1 not in dict1:
        print('学生不存在')
    else :
        dict1.pop(stu1)
def check():
    print(dict1.items())
def infor():
    stu1 = input('学生姓名:')
    if stu1 in dict1:
        cro = input(f'请输入{stu1}的成绩:')
        dict1[stu1] = cro
    else:
          print('学生不存在')
def main():
    print('\n=========学生管理系统==========')
    print('请选择功能\n1:添加学生 2:删除学生 3:查看所有学生 4:录入成绩 5:退出')
    res = int(input('请输入你的选择:'))
    if res == 1:
        add()
    elif res == 2:
        del1()
    elif res == 3:
        check()
    elif res == 4:
        infor()
    elif res == 5:
        return True
    else:
        print('输入有误:')
        return False
while True:
    if not main():
        n = int(input('是否继续:1:yes 2:no:'))
        while   n != 1 and n != 2:
            n = int(input('输入错误请重新输入:'))
        if n == 1:
            continue
        elif n == 2:
            break
    else:
        break
