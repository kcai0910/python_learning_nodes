#集合：无序，元素唯一（自动去重）
# 集合分为两种，分别是可变集合，不可变集合
#可变集合（set）：内部元素无序，不可以通过index来访问，而且 会自动去重
#不可变集合(forzenset)：特点和可变集合一样，元素不可以修改
s1 = {10,20,30,40,50,60,70,80,90,20,10,40}
s2 = {'你好','hello','python'}
s3 = {10,'python',12.5,True}
print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))
#定义空集合不能直接使用{}，否则会变成字典
s4 = set()
print(s4,type(s4))

s5 = frozenset({10,20,30,30,40,50,10})
s6 = frozenset({'你好','hello','python'})
s7 = frozenset({'你好',10,20.5,True})
print(s5,type(s5))
print(s6,type(s6))
#frozenset 接受的参数，可以是任意的可迭代对象，最终返回的一定是不可变集合
s8 = frozenset([10,20,30,30,40,50,60])
s9 = frozenset((10,20,30,30,40,50,60))
s10 = frozenset('python')
print(s8,type(s8))
print(s9,type(s9))
print(s10,type(s10))
#定义不可变空集合
s11 = frozenset()
print(s11,type(s11))
