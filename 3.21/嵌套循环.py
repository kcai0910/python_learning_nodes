
"""
每天学习五个单词，学习七天
"""
for i in range(1,8):
    print(f'这是循环的第{i}天')
    for j in range(1,6):
        print(f'这是第{i}天的第{j}个单词')

"""
终止循环
continue:跳过本次循环，直接进入下一次循环
break:立即终止循环，不再执行后续的代码
"""


for i in range(1,10):
    for j in range(1,10):
        if (i <j):
            break;
        print(f'{i}*{j}={i*j}',end='\t')
    print()