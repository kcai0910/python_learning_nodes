import sys

num = 10
car = 12_450_000
#科学计数法每隔三位加一个下划线
print(car)
print(type(car))

#解除最大数限制
a = 3 ** 2
b = 2 ** 3
sys.set_int_max_str_digits(0) #设置为0表示不做任何限制
# 并不是说python最大值有4300，而是当我们把打印删掉后，代码依然可以执行
#为什么会报错，是因为打印的时候把类型转成了字符串类型来输出
# python3.11 ，对字符串的长度进行限制，最大长度为4300
c = 9 ** 9999
d = c + 100
print(a,b)
print(d)

