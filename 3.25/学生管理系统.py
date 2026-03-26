""""""
"""
1,添加学生
2：删除学生
3：查看所有学生
4：录入成绩
5：退出系统
"""
student = []
def add_stu():
    print('添加学生')
    id_stu = input('请输入学生学号:')
    for i in student:
        if i['id'] == id_stu:
            print('此学号已被录入')
            return
    name = input('请输入学生姓名')
    student.append({'id':id_stu,'name':name,'score':0})
    print('已成功添加信息')

def del_stu():
    print('删除学生')
    id = input('请输入删除学生的学号:')
    for i in student:
        if i['id'] == id:
            student.remove(i)
            print('删除成功')
            return
    print('未找到改学号的学生')

def view_stu():
    print('查看学生')
    if  not student:
        print('未录入学生信息')
        return
    for i in student:
        print(f'学号:{i['id']}',end='\t')
        print(f'姓名:{i['name']}',end='\t')
        print(f'成绩:{i['score']}',end='\n')

def infor_stu():
    print('录入学生成绩')
    id = input('请输入需要录入成绩的学号:')
    for i in student:
        if i['id'] == id:
            score = input('请输入学生的成绩:')
            i['score'] = score
            print('成功录入成绩')
            return
    print('未找到改学号的学生')
def main():
    print('1:添加学生\t2:删除学生\t3:查看所有学生\t4:录入成绩\t5:退出系统')
    res = input('请输入你的操作:')
    if res == '1' :
        add_stu()
    elif res == '2':
        del_stu()
    elif res == '3':
        view_stu()
    elif res == '4':
        infor_stu()
    elif res == '5':
        print('退出')
        return True
    else:
        print('输入错误，请重新输入')
print('---------------学生管理系统---------------')
while True:
    result = main()
    if  result:
        break;