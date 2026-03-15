color = ['red','green','blue','black','orange']
index = 0
#使用while循环遍历 (需要自己维护)
while index < len(color):
    print(color[index])
    index += 1

#使用for循环遍历列表
print("=========================")
for i in color:
    print(i)

#使用for循环
print("=========================")
for k in range(len(color)):
    print(color[k])