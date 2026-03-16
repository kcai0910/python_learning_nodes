"""
set.add(值) :向集合里添加一个值
set.update(可迭代对象) :向集合添加值（必须是一个可迭代对象，比如列表，元组，集合）

set.remove(值) ：在集合中删除指定元素，若值不存在会报错
set.discard(值) ：在集合中删除指定值，若值不存在不会报错
set.pop :在集合中随机删除，返回删除的值
set.clear() :清空集合

由于集合 当中没有下标，所以没有改的方法，但可以结合remove+add来实现修改功能

使用成员运算符来实现查询的功能 in ,not in； 返回结果为bool值
"""
#集合-增
s1 = {10,20,30,40,50}
s1.add(60)
s1.update([70,80])
s1.update((90,100))#只能存放可迭代对象
s1.update({11,22,33})
print(s1)

#集合-删除
s1.remove(11)#删除不纯在元素会报错
s1.discard(22)#删除不纯在discard不会报错
s1.discard(222)
res = s1.pop()#删除任意一个元素,有返回值
# s1.clear()#清空整个集合
print(res)
print(s1)

#集合-修改 通过删除和添加的方式进行修改的
s1.remove(80)
print(s1)
s1.add(800)
print(s1)

#查询 成员运算符
res2 = 2009 in s1
res3 = 200 not in s1
print(res3)