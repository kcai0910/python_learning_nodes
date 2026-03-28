""""""
"""
实例方法:在类里面定义的方法,是为实例服务的，所以也被称为实例方法
因为接收到了self参数，所以内部可以访问实例属性，调用实例方法
"""
class Person:
    plant = '地球'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #实例方法，保存在类身上，主要是给实例提供调用
    def speak(self,msg):
        print('************',self.plant)
        print(f'{self.name},{self.age},{msg}')


p1 =  Person('张三',18)
p2 =  Person('李四',20)
# print(p1.__dict__)
# print(Person.__dict__)

#通过实例可以调用实例方法
p1.speak('我是实例调用')
#通过类是可以调用实例方法的不推荐
Person.speak(p1,'我是类调用')