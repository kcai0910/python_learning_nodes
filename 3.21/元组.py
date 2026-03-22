"""
元组:元组是用来存放一组有序的数据，元组一旦被创建就不可修改(不能增，删，改，只能查)
"""
t1 = (10,20,30,40,50)
t2 = ('web','ui','java','python')
t3 = (100,True,'你好',[1,2,3])
print(t1,type(t1))
print(t2,type(t2))
print(t3,type(t3))

#定义一个空元组
t4 = ()
t5 = tuple()

#定义一个一元素元组,当元组里面只有一个数据时，末尾要添加逗号
t6 = (3,)
print(t6,type(t6))

#元组查看
print(t1[0])

#元组嵌套
t4 = (10,20,30,40,50,(100,200,300))
print(t4[-1])

stu =  ('果子','果子','阿杰','董小姐','玉鹏','超然')
#查看元素第一次出现的下标
res = stu.index('果子')
print(res)
#统计元素出现的次数
res2 = stu.count('果子')
print(res2)
#最大值，最小值，长度，求和,排序(对元组进行排序,返回的是一个新的列表)
print(max(stu))
print(min(stu))
print(len(stu))
print(sum(t1))
print(sorted(t1,reverse = True))
print(t1)

#元组的遍历
index1 = 0
while index1 < len(t1):
    print(t1[index1])
    index1 +=1
for i in stu:
    print(i)

"""
元组特点
1，元组可以存放不同类型的数据
2，元素是有序存储的（正索引和负索引）
3，元组中的数据可以重复
4，元组数据不可以修改，只能查看，                    列表可以修改
5，元组的长度是固定的（一旦创建则不可以修改）           列表长度不固定
"""