# score = int(input('请输入你的成绩:'))
# if score >= 90:
#     print('你的成绩优秀')
# elif score>=80:
#     print('很好')
# elif score>=70:
#     print('良好')
# elif score>=60:
#     print('及格')
# else:
#     print('不及格')


age = int(input('请输入您的年龄:'))
gender = input('请输入您的性别:')
if age >=18:
    print('您成年了')
    if gender == '男':
        print('你是男大')
    elif gender == '女':
        print('你是女大')
    else:
        print('你是小男娘')
else:
    print('未成年')
    if gender == '男':
        print('你是小男孩')
    else:
        print('你是小女孩')