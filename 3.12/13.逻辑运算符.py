# and : 逻辑与，判断两边的值是否都为True,一假则假
print('逻辑与and :')
print(True and True)
print(True and False)
print(False and False)
print("\n举例 :")
print(8>7 and 8>6)
print(8>7 and 8>10)

# or : 逻辑或，判断 两边的值是否至少有一个为True
print("\n逻辑或or :")
print(True or True)
print(True or False)
print(False or False)

print('\n判断 :')
print(8>7 or 8>6)
print(8>17 or 8>6)
print(8>17 or 8>16)

#逻辑and与or都具有逻辑短路功能->只要有一侧结果出来后后续的代码将不再实行

print(False and 3/0)
print(True or 3/0)

# not : 逻辑非,对一个值进行取反
print("\n逻辑非not :")
print(not True)
print(not False)
print(not 3>2)
print(not 'abc')
print(not '')
print(not ' ')
#如果判断条件为运算表达式，则返回计算的结果
print(3+4 and 2+4)
print(3+4 or 2+4)
print(3+4 and True)
print('------------------')
print(6>8 or '')
print(3-4 and 2-3)
print('我' or '你')
print(not 100-100)
print(False or 2-2)
