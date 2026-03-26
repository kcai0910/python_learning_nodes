"""
1，字符串和列表，元组一样支持下标查看
2，字符串不可修改不可嵌套
"""
msg = 'welcome to xszx'
print(msg[-4])
# 1查看指定字符第一次出现的下标
res = msg.index('c')
print(res)
# 2按照指定字符分割字符串,返回的是一个列表
msg2 = 'python@java@web@ui'
print(msg2.split('@'))
# 3替换指定字符为新的字符,返回的是一个新的字符,不会对原来的字符进行修改
msg3 = msg2.replace('@','$')
print(msg3)
# 4统计指定字符出现的次数
res4 = msg2.count('@')
print(res4)
# 5从字符串的两端开始删除指定字符，直到第一个字符不为指定字符为止
msg5 = '666新思字徐666止血66'
res5 = msg5.strip('6')
print(res5)
#内置方法
print(max(msg))
print(min(msg))
print(len(msg))
print(sorted(msg))

#while 循环遍历
index1 = 0
while index1<len(msg):
    print(msg[index1])
    index1 += 1
for i in msg:
    print(i)
