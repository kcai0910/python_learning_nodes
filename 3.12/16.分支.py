#顺序结构-分支结构-循环结构
#python代码是通过代码缩进/空格来识别代码范围
"""
if 判断条件：
      条件满足执行的代码
else:
       条件不满足执行的代码
"""

# if False:
#     print('可以执行1')#归if管
# print('可以执行2')#不归if管
age = int(input('请输入您的年龄:'))
# 单分支
# if age>=18:
#       print('你是成年人')
# 双分支
if age >= 18:
    print('你是成年人')
else:
    print('你是未成年人，需要好好学习')