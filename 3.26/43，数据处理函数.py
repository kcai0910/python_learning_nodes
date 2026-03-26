""""""
"""
map():对一组数据中的每一个元素统一执行某一个操作，并生成一组新的数据
map(操作函数,可迭代对象)
map函数返回的是一组迭代器对象，需要我们自己手动遍历，或者类型转换，数据会被消耗（只能使用一次）
"""
num = [10,20,30,40,50]
def double(n):
    return n*2
res = map(double,num)

for i in res:
    print(i)
print(res)
# 迭代器对象是可以被消耗的
print(list(res))
res2 = map(lambda x:x*2,num)
print(res2)
print(list(res2))

a = 'hyx'
z = a.upper()
print(z)
#字符串统一转换
names = ('hyx','xszx','python')
res3  = map(lambda x:x.upper(),names)
print(tuple(res3))

number = {'1','2','3'}
res4 = map(int,number)
print(list(res4))
"""
注意事项
1：延迟执行，map不会立刻计算，只有在需要结果的地方才执行
2：返回的是迭代器对象，一旦被使用则会被耗尽
3：map函数不会影响元素的数量
"""
l1 = [[1,4,21,2,1,3],[133,2333,211,323,12]]
res5 =map(sorted,l1)
print(list(res5))