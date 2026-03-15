"""
1，录入多名同学的成绩
2，输出统计平均分
3，输出统计合格人数
4，输出最高分
5，输出最低分
"""

# score = ''
# score_list = []
# pass_count = 0
# while True:
#     score = input("请输入成绩:")
#     if score == '#':
#         break
#     else:
#         score_list.append(int(score))
#         if  int(score)> 60:
#             pass_count +=1
# if score_list:
#     print(f'平均分:{sum(score_list) / len(score_list)}\n合格人数:{pass_count}\n最高分:{max(score_list)}\n最低分:{min(score_list)}')
# else:
#     print('请重新录入成绩')



print('请输入学生的成绩，输入"q"终止')
#变量输入的成绩
score_list = []
#循环输入成绩
while True:
    data = input('请输入成绩:')
    if data == 'q':
        break
    else:
        score_list.append(int(data))
print(score_list)
#列表里有数据才能进入分支结构
if score_list:
    # 统计平均分
    avg = sum(score_list)/len(score_list)
    pass_count = 0
    for i in score_list:
        if i >60 :
            pass_count += 1
    print(f'总人数为{len(score_list)}')
    print(f'平均分为:{avg}')
    print(f'及格人数为:{pass_count}')
    print(f'最高分:{max(score_list)}')
    print(f'最低分:{min(score_list)}')
else:
    print('请重新录入成绩')
