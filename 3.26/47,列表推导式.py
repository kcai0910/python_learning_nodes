""""""
"""
列表推导式：
概念：用一条简洁的语句，从可迭代对象里，生成新列表的语法结构
语法结构[表达式 for 遍历 in 可迭代对象]
"""
num = [1,2,3,4,5,6]
res2 = [i*2 for i in num]
print(res2)
#带条件的列表推导式
res3 = [i*2 for i in num if i>3]
print(res3)

#字典推导式
names = ['果子','水哥','张强']
score = [80,90,99]

res4 = {names[i]:score[i] for i in range(len(names))}
print(res4)

#集合推导式
names2 = ['果子','水哥','张强']
res5 = {a  for a in names2}
print(res5)
print(type(res5))

#元组推导式
names3 = ['果子','水哥','张强']
#python里面没有元组推导式，下面这种写法是:生成器
res6 = (i for i in names3)
print(res6)
print(tuple(res6))