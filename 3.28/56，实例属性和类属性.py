""""""
"""
实例属性，通过（实例.属性名= 值） 定义实例身上的属性，称为实例属性
特点:1每个实例身上的属性，都是独立的，实例之间互不影响
2:实例属性只能通过[实例.属性 = 值]的形式来访问和修改

类属性:定义在类里面的属性就是类属性
1：所有实例都可以访问，可以理解为公共数据
2：类属性既可以类来访问，也可以通过实例来访问
"""

class Person:
    max_age = 18
    plant = '地球'
    def __init__(self,name,age,gender):
        self.name = name
        self.gender = gender
        if age <= Person.max_age:
            self.age = age
        else:
            print('你的年龄很大了')
            self.age = 120

p1 = Person('水哥',18,'男')
p2 = Person('张强',20,'男')

print(p2.name)
p1.name = '水哥2'
print(p1.name)
#验证实例身上没有类属性
print('验证实例身上没有类属性')
print(p1.__dict__)
print(p2.__dict__)
#验证所有实例都可以访问类属性
print('验证所有实例都可以访问类属性')
print(p1.max_age) #1,先查找实例自身是否有max_age属性 2：查找类身上是否有max_age属性
print(p2.plant)

#验证通过类来访问类属性
print('验证通过类来访问类属性')
print(Person.max_age)
print(Person.plant)

#当进行 实例.属性 = 值 操作时，只会对实例自身起作用（有就修改没有就添加）
print(p1.__dict__)
p1.plant = '火星'
print(Person.plant)
print(p1.plant)
print(p2.plant)
print(p1.__dict__)