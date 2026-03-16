info = {
    'name':'渠江涛',
    'age':18,
    'obj':'python'
}
#字典添加,如果字典里有就是修改，如果字典里没有就是添加
info['hobby'] = ['learn','sing']
#字典删除
del info['age'] #删除指定key
res = info.pop('hobby') #删除指定key,并返回删除key对应的value
res2 = info.pop('height','删除失败') #如果删除一个不存在的key,那么可以设置一个默认报错信息，不然代码会报错
# info.clear()#清空字典

info['name'] = 'hy'
#字典修改
info.update({'name':'hyx2','obj':'web'}) #批量修改多个key值

print(info,type(info))

#查询
print(info['name'])
# print(info['height'])#查询一个不存在的key会报错
res5 = info.get('height','height不存在')#查询一个不存在的key会提示默认值
print(res5)

#1使用keys方法,获取字典中的所有键(key)
#返回的是一种叫做dict_keys的类型，不是列表类型
res6 = info.keys()
print(res6,type(res6))
#dict_keys和列表类似,可以被遍历。但是他不能通过下标来访问
for k in res6:
    print(k)
# print(res6[0])
l1 = list(res6)
print(type(l1),l1)
#2使用value方法，获取字典中所有的值
res7 = info.values()
print(type(res7),res7)

#使用items方法，可以获取字典中所有键值对(每个键值对是元组形式)
res8 = info.items()
print(type(res8),res8)

for i in info:
    print(i)
    print(info[i])

"""
1,字典是以键值对的形式存在，每个键都对应的一个值
2，字典里的key不能重复，若重复后面的会覆盖前面的
3，键不可改变，必须是不可变类型，值可以是任意类型
4，不支持下标，字典无法通过下标取值
5，支持增删改查，支持for循环遍历
"""

"""
数据容器:列表（list），元组(tuple)，字符串(str)，集合(set)，字典(dict)
有序:列表，元组，字符串 可通过下标来访问
无序:集合，字典  元素没有固定位置，不能用下标来访问

可变：集合，集合，字典 可对内容进行增删改查
不可变 元组，frozenset(),字符串 内容固定创建后无法修改

允许重复：列表，元组，字符串
不允许重复:集合，字典（key不允许但是value可以重复）
"""
