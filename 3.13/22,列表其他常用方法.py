"""
list.index(值) 查找元素第一词出现的下标
list.count(值) 统计元素在列表当中出现的次数
list.reverse() 反转列表,不需要参数，直接操作原列表
list.sort(reverse=布尔值)    对列表进行排序默认从小到大，会改变原列表
"""


color = ['red','green','blue','yellow','red']
res = color.index('blue')
res2 = color.count('yellow') #统计元素出现的次数
print(res2)
num = [10,50,40,80,[11,22,33,44,40,50]]
num.reverse()
num[0].reverse()
print(num)

num2 = [10,50,20,80,70,30,40]
num2.sort(reverse=True) #True从大到小,False 从小到大
print(num2)

#排序必须纯整形纯字符串

num3 = ['hyx','xszx','px','z','t']
num3.sort()
print(num3)

