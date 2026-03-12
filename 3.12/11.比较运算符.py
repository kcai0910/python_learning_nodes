"""
% 取余运算   //取整
**指数运算
赋值运算
+= -= *= /= **= //= %=
==判断左右两侧是否相等
！=判断不等
"""

# == 判断左右两侧的值是否相等
a = 5
b = 7
c = '5'
res = a == b
res2 = a == c
print(res)   #false
print(res2)  #false

# !=判断左右两侧的值是否不等
res = a != b
res2 = a != c
print(res)   #true
print(res2)  #true

# >:判断左侧的值是否大于右侧
res3 = a > b
print(res3)  #false
# res4 = a > c #整形和字符串无法进行大小比较
res5 = a < b
# re6 = a <= c  #整形和字符串无法进行大小比较
print(res5)   #true

res7 = a >= 7
res8 = a <= 7
print(res7)  #false
print(res8)  #ture

#字符串在对比时优先对比unicode码
d = 'abc'
e = 'abc'
print(d == e) #ture

print(ord('a')) #97   ord查看汉字和字母的unicode 码
print(ord('我')) #25105

str1 = '我爱你'
str2 = '我爱他'
print(str1 == str2)
print(str1 > str2)
print(ord('你'))
print(ord('他'))
print(chr(97))
print(chr(25105))
print(chr(100))

#ord() :用来查看unicode码
#chr() :用来将unicode码转为字符

print(f'{ord('渠')}{ord('江')}{ord('涛')}')
print(ord('渠'),ord('江'),ord('涛'))
print(chr(28192))
print(chr(27743))
print(chr(28059))