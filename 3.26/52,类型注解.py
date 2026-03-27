""""""
"""
1,类型注解不会影响程序，它是给程序和开发人员用的 
"""
num:int = 10
price:float = 10
msg:str = '你好'
msg = 10
is_vip:bool = True
res:None = None

#先写变量的类型注解，以后在赋值
#并不是在定义变量，它只是说明
# name:str
# print(name)
#name = 10
# print(name)
#对列表中的元素进行限制应该为字符串
hobby:list[str] = ['抽烟','喝酒','烫头',10]
# 对列表中的元素进行限制应该为字符串与整形
hobby2:list[str | int] = [10.5,2.5]
print(hobby)

hobby3:list[Union[str,int]] = [18.5,10]
#对字典进行类型注解
s1:dict[int,int] = {20:10}
s1:dict[int|str,int] ={10.5:10}

#元组比较特殊
#是对元组类型进行注解而且是对一个元素进行注解
t1:tuple[int,int] = ( 10,10)
t2:tuple[int,...]=(10,20,30)
t3:tuple[int|str,...]=(10,20,30,'hello')

#pythomn里提供类型推导，根据变量初始赋值的实际数据，自动推断变量的类型
x = 100
x ='你好'

y = [10,20,30]
y.append('40')
print(y)

def add(a:int,b:int)->int:
    return a+b
res = add('10','20')
print(res)

