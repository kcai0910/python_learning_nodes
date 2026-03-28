""""""
from  datetime import datetime
"""
静态方法:通过@staticmethod,方法没有self,cls参数，只是单纯的定义在类里
1，可以通过类和实例调用
2：由于没有self和cls参数，所以不能访问类属性，实例属性

#定义在类里面的一个静态方法，用于处理类相关的业务

实例方法
    1：可以接收self参数，所以可以访问实例属性
    2：主要是为实例对象提供服务的
类方法@classmethod
    1：可以接收cls参数，所以可以访问类属性
    2：主要是为类服务的
静态方法：@staticmethod
    1：没有参数，所以无法访问类属性实例属性
    2.用于处理与类相关的业务
"""
class Person:
    max_age = 150
    plant = '地球'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        res = current_year -year
        if res>=18:
            print('你成年了')
        else:
            print('未成年')
        print(res)
        print('我是静态方法')
        pass

p1 =  Person('张三',18)
p2 =  Person('李四',20)

#验证静态方法也存在类身上
print(Person.__dict__)
#验证类可以访问静态方法
Person.is_adult(1998)
#验证实例可以访问静态方法
p1.is_adult(1995)