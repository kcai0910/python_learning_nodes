""""""
"""
1:可以存放多个数据，每一个数据都被称为元素
2，数据容器中的元素可以是任意类型
3，数据容器会给我们提供多个操作元素的方法
#在python里的数据容器
列表(list) 元组(tuple) 字符串(str) 集合(set) 字典(dict)
"""

#列表就是用来存放一组有序的数据，而且可以对其的数据进行增删改查
#定义一个列表
list1 = []

#下标也被称为索引，就是元素在列表中的位置编号，分为正索引和负索引
#通过下标取值时，不要超过列表范围，否则会报错

stu =  ['果子','阿杰','董小姐','玉鹏','超然']
#列表添加1
stu.append('阿强')
#列表添加2
stu.insert(2,'张淼')
#列表添加3
#添加的是可迭代对象
stu.extend('teet')

#列表删除1 删除指定位置的元素，并且将删除的元素返回
#有返回值,返回删除的结果
res = stu.pop(1)
print(res)
#列表删除2
#remove 删除的是列表第一次出现的值
stu.remove('果子')
#列表删除3 清空整个列表
# stu.clear()
#列表删除4 删除指定位置的元素
del stu[3]

#列表修改
stu[-1] = 'orange'
#列表查看
print(stu[-1])
print(stu)

#列表其他常用方法
#查找元素第一次出现的下标
res = stu.index('阿强')
#统计元素在列表里面出现的次数
res2 = stu.count('e')
#对列表里面的元素进行反转，不需要参数，直接操作的原列表
stu.reverse()
#对列表进行排序,默认从小到大 会改变圆列表，如果列表里面有多个数据类型的元素，会报错，字符串先转unicode码然后再对比
stu.sort(reverse = True)
print(res)
print(res2)
print(stu)

#列表内置方法
num = [1,2,3,4,5]
#最大值
print(max(stu))
#最小值
print(min(stu))
#长度
print(len(stu))
#求和
print(sum(num))


#while循环遍历
index1 = 0
while index1<len(stu):
    print(stu[index1],end=' ')
    index1 += 1
print()

for i in stu:
    print(i,end=' ')

"""列表的特带你:
1:可以存放不同类型的元素，
2:元素是有顺序的（正索引和负索引）
3:列表中的元素是可以重复的
4:列表可以增删改查
5:列表长度不固定，可以随意操作"""