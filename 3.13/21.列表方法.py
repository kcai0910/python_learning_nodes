"""
#新增
list.append(值) 列表末尾添加
list.insert(下标，值)  列表指定位置插入
list.extend(可迭代对象) 列表末尾追加可迭代对象

#删除
list.pop(索引) 删除指定位置的元素，并将删除的元素返回
list。remove(值) 删除列表第一次出现的指定值
lisst.clear() 清空列表
del list(下标) 删除指定位置的元素

#修改
list[索引] = 新值

#查看
list[下标]
list[下标][下标]
"""


#  列表新增
num = [10,20,30,40,50]
#列表末尾添加
num.append(60)
print(num)
#指定下标处添加元素
num.insert(1,100)
print(num)
#把可迭代对象最加到num的末尾
num.extend('hyx')
num.extend(['one','two','three'])
print(num)

#  列表删除
#pop 删除一个元素
res = num.pop(-1)
print(res)
#remove 删除的是第一次出现的值
num.remove(60)
print(num)

#del删除指定位置的元素
del num[5]
print(num)

#清空所有元素
# num.clear()
# print(num)

#  列表改
num[-2] = 99
num[1] = 200
print(num)

#列表查
print(num[6])
print(num[-5])

num2 = [10,20,30,40,50,66,['red','blue','green','yellow']]
print(num2[6][-1])
num2[-1].append('orange')
print(num2[6])
num2[-1].pop(2)
print(num2[6])
num2[6][-1] = 'black'
print(num2[6])

