#数据类型转化
#ex:用户输入的都是字符串，若进行数据运算，必须转数据类型
#ex:使用数据库数据时，也会进行数据类型转换
"""
str(x):可以将任意一个数据类型转化为字符串类型
int(x):带有中文的值，字符串的浮点型，不可转换
       两边带有空格数字，字符串的纯数字，整数类型都可以转
float(x)：中间带有空格数字，带有汉字的值，不可以转
        纯数字，整体，浮点型都可以转
"""
num = '18.5'
num2 = '18'
print(type(str(num)))

age = 18
height = 175.5

print(type(str(age)))
print(type(str(height)))
#将任意一个数据转成字符串
print(type(int(age)))
#print(type(str(num)))#带小数点的字符串不能转整形
print(type(int(height)))
#不能将字符串转整形
print(type(float(height)))
print(type(float(age)))
print(type(float(num)))
print(type(float(num2)))
#不带小数点的字符串可以转整形
print(type(int(num2)))

print("练习\n")
print("转整形")
print(type(int(8)))
print(type(int(8.5)))
print(type(int('8')))
print(type(int('  8  ')))
#print(type(int('  8 2  ')))
#print(type(int('  8.2  ')))
#print(type(int('abc')))
#print(type(int("数量")))

print("\n转浮点型")
print(type(float(8)))
print(type(float(8.2)))
print(type(float('   8.2   ')))
#print(type(float('   8 .2   ')))
#print(type(float('abd')))

print("/n转字符串")
print(type(str(2)))
print(type(str(2.5)))
print(type(str('acasd')))