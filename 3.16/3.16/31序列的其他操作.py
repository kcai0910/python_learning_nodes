#只用同类型的序列才能相加
list1 = [10,20,30]
list2 = [40,50,60]
t1 = (30,40,50)
t2 = (50,60,70)
s1 = 'hello'
s2 = 'world'
res = list1+list2
print(res)
res2 = t1 + t2
print(res2)
res3 = s1+s2
print(res3)
# res4 = list1 + t1
# print(res4)
#序列相乘，把序列重复指定次数
res5 = t1 * 5
res6 = list1 * 2
res7 = s1 * 2
print(res5)
print(res6)
print(res7)