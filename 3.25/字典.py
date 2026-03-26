""""""
"""
字典:用來存放一組鍵值對的數據,可以通過鍵對值進行增刪改查
1，字典中的鍵不能重複，如果重複後面的值會覆蓋前面的
2,字典中的key必须是不可变类型，但value可以是任意类型
3,字典是可以嵌套的
"""
d1 = {'張三':18,'李四':19,'王五':20,'張三':21}
print(type(d1))
print(d1)
#定義空字典
d2 = {}
d3 = dict()
print(type(d2),type(d3))

#字典方法
stu = {
    'name' : '玉鹏',
    'age' : 18,
    'height':176.5
}
#字典添加
stu['hobby'] = ['抽烟','喝酒','烫头']
stu['weight'] = 160
print(stu)
#字典删除
del stu['hobby']
res = stu.pop('weight')#删除指定key，并返回删除key所对应的value
res2 = stu.pop('id','删除失败')#如果删除一个不存在的key,会报错.如果有提示信息则返回提示
#清空字典
# stu.clear()
print(stu)
print(res2)

#字典修改 (如果key存在就是修改，如果不存在就是添加)
stu['age'] =  19
stu['money'] = 500
print(stu)
stu.update({'name':'家和','age':21,'height':180})
print(stu)

#字典查看(根据键来查，返回的是value,如果查看一个不存在的key会报错)
res5 = stu['name']
res7 = stu.get('hobby','报错提示')
print(res7)

#1:使用keys方法，获取字典中所有的键
#返回的并不是一个列表类型的数据，而是一种叫做dict_keys的类型
re = stu.keys()
print(re)
#使用value方法，可以获取字典中所有的值
re2 =stu.values()
print(re2)
#使用items可以获取字典中所有的键值对
re3 = stu.items()
print(re3)
# 遍历列表遍历
for i in stu:
    print(i,'\t',stu[i])