"""
1：字符串：只要是被引号包裹的，都属于字符串
2：整数：只要没有小数点的数字都属于整形
3：浮点型:只要是带小数点的数字都属于浮点型
判断数据类型使用：type()"""
name = '哞哞牟'
age = 19.0
weight = 40

res = type(name)
res1 = type(age)
res2 = type(weight)
print(res)
print(res1)
print(res2)

