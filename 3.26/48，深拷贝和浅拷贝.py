l1  = [10,20,30,40]
#是赋值不是复制
l2 = l1
l1[2] = 100
print(l1)
print(l2)
print(id(l1))
print(id(l2))
#两个变量指向了同一个对象，修改其中一个会互相影响

#浅拷贝
#会创建一个新的外层容器，但是内部元素任然使用的是原来的对象
#嵌套数据仍然是共享的，修改嵌套数据仍然会互相影响
import copy
list1 = [10,20,30,40,[50,60]]
list2 =  copy.copy(list1)
list1[0] = 100
list1[4][1]=100
print(list1)
print(list2)
print(id(list1))
print(id(list2))
print(id(list1[4]))
print(id(list2[4]))

#深拷贝
#创建一个新的外部容器，并对其内部所有对象进行复制
list2 = copy.deepcopy(list1)
list1[4][1]=200
print(list1)
print(list2)
print(id(list1[4]))
print(id(list2[4]))
#深拷贝可以彻底消除数据之间的相互影响
