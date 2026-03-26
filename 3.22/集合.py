""""""
"""
集合是一种无序，元素唯一的数据类型。
补充，在集合里如果1与True同时存在，也被集合自动去重，谁在前面展示谁，同理0和False也一样
原理为：布尔值（True和False）为整型的子类型
集合分为两种，
可变集合（set）:内部的元素无序，不能通过下标来访问，会自动去重
不可变集合(frozenset):特点和可变集合一样，唯一的区别是元素不可修改
"""
# 定义可变集合
list1  = {True,1,0,False,10, 20, 30, 40, 50,60,60}
print(list1)
# 不能使用{}来定义空集合，因为直接写{}是字典
# s4 = {}
# 定义空集合
s5 = set()
# print(type(s4),s4)
print(type(s5),s5)

#定义不可变集合(需要借助frozenset()这个方法)
# frozenset接收的参数，可以是任意可迭代对象
s6 = frozenset({12,3,4,5})
print(type(s6),s6)

# 集合的嵌套问题
one = {10,20,30,40}
two = frozenset({100,200,300,400,500})
li = [111,222,333,444]
t1 = ('helo','world','python')
#集合不可以嵌套可变集合,可以嵌套不可变集合
# 集合不可嵌套可变数据容器,可以嵌套不可变数据容器
#数据容器如果是可变的，那么就不可以防在集合里
three = {11,22,33,t1}
print(three)

# 集合增删改查
s1 = {10, 20, 30, 40}
#集合-增
s1.add(50)
s1.update({4,2,3,1})
print(s1)
#集合-删除 remove删除一个不存在的值会报错 discard 删除一个不存在的值不会报错 pop 随机删除
s1.remove(50)
s1.discard(44)
#pop随机删除，集合为空将会引发错误
res = s1.pop()
# s1.clear()
print(s1)
print(res)

# 集合修改 借助添加删除两个方法来实现修改的功能
s1.remove(10)
s1.add(50)
print(s1)
#集合查
#使用成员运算符来实现查询功能
# in  和 not in
res3 = 30   in  s1
print(res3)

#集合的常用方法
a1 = {10, 20, 30, 40, 50}
a2 = {30,40,50,60,70}
# 在a1集合里面不同与a2的数据 (右返回值，返回不同的数据)
res = a1.difference(a2)
res4 = a1 - a2
print(res)
print(res4)
# 在a1里面删除a2存在的数据 (没有返回值，操作的是原集合)
a1.difference_update(a2)
print(a1)
#合并两个集合 自动去重 （返回一个新集合，并且自动去重）
res2 = a1.union(a2)
res3 = a1|a2
print(res2)
print(res3)

a3 = {10,20,30,40,50}
a4 = {30,40,50,60,70}
a5 = {30,40,50}
a6 = {80,90}
#判断a5是否为a3的子集
res5 = a5.issubset(a3)
print(res5)
#判断a4是否是a5的超集
res6 = a4.issuperset(a5)
print(res6)
#判断是否没有交集
res7 = a3.isdisjoint(a4)
print(res7)

#集合数学运算符
s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}
#并集(|)合并两个集合
res = s1 | s2
print(res)
#交集(&)返回两个集合同时拥有的数据
res2 = s1 & s2
print(res2)
#差集(-) 在s1中拥有的，但是集合s2中没有的
res3 = s1 - s2
print(res3)
#对称差集(^) 返回一个没有交集的数据
res4 = s1 ^ s2
print(res4)

# 集合的遍历
for item in s1:
    print(item)

"""
1，无序，集合中的元素没有固定顺序，无法通过下标来访问
2，不重复，集合会自动去重
3，集合分为两个类型，可变集合（set）不可变集合（frozenset）
4,集合中的元素必须是不可变类型的（元组，字符串，不可变集合，数字）
5，集合支持数学运算
"""