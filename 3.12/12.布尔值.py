#布尔类型 ：True False
# ：条件是否成立，事件是否发生，操作是否成功，逻辑等功能
a = True
b = False
c = 5 > 7
print(a,b,c)
print(type(a),type(b),type(c))
#布尔类型是int的子类型
print(int(True))
print(int(False))
#所以布尔值可以参与运算
print(1 + True)
print(7 - False)
print(True + False)
print(True + True)
print(2 > True)
print(False <= 0)
#转布尔值(非0的数字转布尔值都为True，非空的字符串转布尔值都为True)
print(bool(1))
print(bool(0))
print(bool(100))
print(bool(25.6))
print(bool(-8))
print(bool('0'))
print(bool('hello'))
print(bool('avd'))#True
print(bool(''))#False
print(bool('  '))#True
print(bool()) #False