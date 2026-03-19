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
# dict1 = {}
# def add():
#     stu1 = input('学生姓名:')
#     dict1[stu1] = None
# def del1() :
#     stu1 = input('请输入需要删除的学生姓名:')
#     if stu1 not in dict1:
#         print('学生不存在')
#     else :
#         dict1.pop(stu1)
# def check():
#     print(dict1.items())
# def infor():
#     stu1 = input('学生姓名:')
#     if stu1 in dict1:
#         cro = input(f'请输入{stu1}的成绩:')
#         dict1[stu1] = cro
#     else:
#           print('学生不存在')
# def main():
#     print('\n=========学生管理系统==========')
#     print('请选择功能\n1:添加学生 2:删除学生 3:查看所有学生 4:录入成绩 5:退出')
#     res = int(input('请输入你的选择:'))
#     if res == 1:
#         add()
#     elif res == 2:
#         del1()
#     elif res == 3:
#         check()
#     elif res == 4:
#         infor()
#     elif res == 5:
#         return True
#     else:
#         print('输入有误:')
#         return False
# while True:
#     if not main():
#         n = int(input('是否继续:1:yes 2:no:'))
#         while   n != 1 and n != 2:
#             n = int(input('输入错误请重新输入:'))
#         if n == 1:
#             continue
#         elif n == 2:
#             break
#     else:
#         break

#定义一个学生数据容器
students = []
def add_stu():
    print('😀添加学生')
    stu_id = input('请输入你的学号:')
    #学号是否重复
    for stu in students:
        if stu['id'] == stu_id:
            print('学号已存在，添加失败!❌')
            return
    stu_name = input('请输入你的姓名')
    students.append({'id': stu_id, 'name': stu_name,'score':''})

def del_stu():
    print('删除学生')
    if not students:
        print('暂无学生信息')
        return
    stu_id = input('请输入你要删除的学号:')
    #声名一个变量用于保存索引值
    index = ''
    for i in range (len(students)):
        if students[i]['id'] == stu_id:
            index = i
            break
    if index != '':
        students.pop(index)
        print('删除成功')
    else :
        print('未找到学生❌')

def show_stu():
    print('查看所有学生')
    if not  students:
        print('暂无学生信息')
        return
    print('学号     姓名     成绩')
    for stu in students:
    #<左对齐 >右对齐 ^居中
        print(f'{stu['id']:<8}{stu['name']:<8}{stu['score']:<8}')

def score_stu():
    print('录入成绩')
    if not students:
        print('暂无学生信息')
        return
    stu_id = input('请输入你要录取成绩的学号:')
    for stu in students:
        if stu['id'] == stu_id:
            score = input('请输入成绩:')
            stu['score'] = score
            print('成绩已成功录入')
            return
    print('没有找到该学生😓')

def main():
    print('===========学生管理=========')
    print('1:添加学生 2:删除学生 3:查看所有学生 4:录入成绩 5:退出')
    #用户输入指定操作
    res = input('请输入你的操作:')
    # if res not in ('1', '2', '3', '4', '5'):
    #     print('❌输入有问题,请重新输入 ')
    if res == '1':
       add_stu()
    elif res == '2':
        del_stu()
    elif res == '3':
        show_stu()
    elif res == '4':
        score_stu()
    elif res == '5':
        print('退出')
        return True
    else:
        print('输入错误，请重新输入')
while True:
    result = main()
    if result :
        break

# def add_stu():
#     print('添加学生😀')
#     stu_id = input('请输入你的学号:')
#     for stu in students:
#         if stu['id'] == stu_id:
#             return
#     stu_name = input('请输入你的姓名:')
#     students.append({'id': stu_id, 'name': stu_name,'score':''})
#     def show_stu():
#         if not students:
#             print('暂无学生信息')
#             return
#         print('学号    姓名    成绩')
#         for stu in students:
#             print(f'{stu["id"]:<8}{stu["name"]:<8}{stu["score"]:<8}')

# def del_stu():
#     if not students:
#         print('暂无学生信息')
#         return
#     index = ''
#     stu_id = input('请输入要删除的学号')
#     for stu in range(len(students)):
#         if students[stu]['id'] == stu_id:
#             index = stu
#             break
#     if index != '':
#         students.pop(index)
#         print('删除成功')
#     else :
#         print('未找到学生❌')


# def score_stu():
#     if not students:
#         print('暂无学生信息')
#         return
#     stu_id = input('请输入你要录取成绩的学号:')
#     for stu in students:
#         if stu['id'] == stu_id:
#             score = input('请输入成绩:')
#             stu['score'] = score
#             return
#     print('没有找到该学生😓')
