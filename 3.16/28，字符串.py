#1,字符串和列表，元组一样，支持下标查看
#2，字符串不可以修改，不可嵌套
msg = 'welcom to xszx'
print(msg[-6])
# msg[0] = 'a'
# msg2 = 'pyt'hyx'hon'

#1 查看指定字符第一次出现的下标
res = msg.index('o')
print(res)
#2 按照指定字符分割字符
msg3 = 'python@ui@web@java'
res2 = msg3.split('@')
res3 = msg.split(' ')
print(res3)
print(type(res2))
#3 替换指定字符为新的字符
res3 = msg.replace('xszx','python')
print(msg)
print(res3)
#4 统计指定字符出现的次数
res4 = msg.count('b')
print(res4)
#5 从字符块两端开始删除指定字符，直到部位指定字符则停下
msg4 = ('6信思666智学66')
res5 = msg4.strip('6')  #从两端开始删
print(res5)

print(len(msg))
print(max(msg))
print(min(msg))
print(ord('z'))
print(ord(' '))
print(sorted(msg,reverse=True))
