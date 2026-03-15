#数据容器可以存放多个数据，每一个数据都被称为元素
#数据容器中的元素可以是任意类型
#数据容器会给我们提供多个操作元素的方法例如：crud

#python中的数据容器有:
# 列表(list),元组(tuple),字符串(str),集合(set),字典(dict)

#列表：就是用来存放一组有序的数据，而且可以对其中的数据进行crud
#定义有内容的列表
list1 = [10,20,30,40,50]
list2 = ['你好','python','天师府','老天师']
list3 = [20,'天师府',True,None,18.5]
list4 = [20,'天师府',True,None,18.5,[10,20,30,40,50]]

#定义空列表
list5 = []
list6 = list()

print(list1,type(list1))
print(list2,type(list2))
print(list3,type(list3))
print(list4,type(list4))
print(list5,type(list5))
print(list6,type(list6))
