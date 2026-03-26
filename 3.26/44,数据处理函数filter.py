""""""
"""
filter():从一组数据里，筛选符合条件的元素（过滤），并返回一组新的数据
#filter(过滤函数，可迭代对象)
filter 会自动赛选函数返回值为True的数据
"""
#普通函数实现
num = [10,20,30,40,50,60]
def test(n):
    if n>30:
        return  n
res = filter(test,num)
for n in res:
    print(n)
print(res)
res2 = filter(lambda n:n>30,num)
print(list(res2))

s1 = [
    {'name':'董小姐','age':18,'score':80},
    {'name':'超然','age':19,'score':90},
    {'name':'赵卿','age':20,'score':95},
    {'name':'赵宁杰','age':21,'score':60},
    {'name':'玉鹏','age':22,'score':50},
    {'name':'水哥','age':23,'score':55}
]
res3 = filter(lambda x:x['score']>=60,s1)
# print(list(res3))
# for i in res3:
#     print(i['name'])
res4 = filter(lambda x:int(x['age'])>=20,s1)
print(list(res4))

#过滤字符串
names = ['','若曦',None,'强',0]
# 过滤条件为假的数据
res6 = filter(lambda n:bool(n)!=False,names)
print(list(res6))
# 如果不传递过滤函数,自动过滤转布尔值为False的数据
res7 = filter(None,names)
print(list(res7))

"""
注意事项
1：延迟执行，filter不会立刻计算，只有在需要结果的地方才执行
2：返回的是迭代器对象，一旦被使用则会被耗尽
3：filter函数会影响元素的数量
"""
