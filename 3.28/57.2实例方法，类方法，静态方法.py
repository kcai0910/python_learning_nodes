""""""
"""
类方法，需要使用装饰器@classmethod ,第一个参数是类本身，通常使用cls接受
"""
class Person:
    max_age = 150
    plant = '地球'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #实例方法，保存在类身上，主要是给实例提供调用
    def speak(self,msg):
        print(f'{self.name},{self.age},{msg}')
    @classmethod
    def change_plant(cls,value):
        cls.plant =value
        print(cls,value)

p1 =  Person('张三',18)
p2 =  Person('李四',20)
#验证类方法是保存在类身上的
print(Person.__dict__)

#通过类来调用类方法
Person.change_plant('月球')
print('*'*20)
#验证类方法改的是类属性的值（根本上变了）
print(Person.plant)
print(p1.plant)

#验证实例也可以调用类方法，但是不推荐
p1.change_plant('火星')
print(Person.plant)