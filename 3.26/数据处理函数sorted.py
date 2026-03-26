""""""
"""
sorted():对一组数据进行排序,返回一组新的数据
语法格式为sorted(可迭代对象,key=可设置排序的依据,reverse=设置排序方向)
"""
#排序依据,reverse可以省略.默认从小到大
num = [10,20,30,90,50,80,60]
res = sorted(num)
#可以设置reverse实现从大到小
res2 = sorted(num,reverse = True)
print(res)
print(res2)

strs = ['python','java','web','js']
res3 = sorted(strs)
res4 = sorted(strs,reverse = True)
res5 = sorted(strs,key=lambda x:len(x),reverse= True)
res6 = sorted(strs,key=len,reverse= True)
print(res3)
print(res5)
print(res6)

#对字典进行排序
s1 = [
    {'name':'董小姐','age':40,'score':80},
    {'name':'超然','age':19,'score':90},
    {'name':'赵卿','age':30,'score':95},
    {'name':'赵宁杰','age':21,'score':60},
    {'name':'玉鹏','age':28,'score':50},
    {'name':'水哥','age':30,'score':55}
]
res7 = sorted(s1,key = lambda x:int(x['age']))
print(res7)
for i in res7:
    print(i['name'])

#max和min,也可以通过设置key传递参数,用于筛选依据
res8 = max(s1,key = lambda x:x['score'])
print(res8)
res9 = min(s1,key = lambda x:x['score'])
print(res9)