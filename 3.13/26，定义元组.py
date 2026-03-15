#定义一个元组
list1 = []
t1 = (11,22,33,44,55)
t2 = ('web','python','ui','java')
t3 = (100,True,'你好',[1,2,3])
print(type(t1),t1)
print(type(t2),t2)
print(type(t3),t3)

t4 = ()
t5 = tuple()
print(type(t4),t4)
print(type(t5),t5)
#元组里面只有一个数据的时候加逗号
t6 = ('你好',)
t7 = (18,)
print(type(t6),t6)
print(type(t7),t7)
#元组的查看
t8 = (11,22,33,44,55,[66,77,88,('你好','python')])
print(t8[-1])
#元组不可修改,如果元组存放了可变类型（列表），那么可变类型是可以修改的
t8[-1][0] = 10
print(t8)
print(t8[-1][3][0])
#查看元素第一次出现的下标
t9 = (10,20,30,40,50,30,20,10,20)
res = t9.index(20)
print(res)
res2 = t9.count(20)
print(res2)

t10 = (10,20,30,40,50)
print(max(t10))
print(min(t10))
print(len(t10))
print(sum(t10))
print(sorted(t10,reverse=True)) #返回的是一个新的列表
print(t10)

num = [10,20,10,30,20,50,30]
print(num)