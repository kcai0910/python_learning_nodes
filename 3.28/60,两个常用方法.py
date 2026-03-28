""""""
"""
isinstance(obj,Class):判断对象是否为指定类或其子类的实例
issubclass(sub,supper):判断一个类是否为另外一个类的子类
"""
class Person:
    def __init__(self,name,age,gender):
        self.name  = name
        self.age = age
        self.gender = gender

    def speak(self,msg):
        print(f'我是Person:我叫{self.name},我今年{self.age},我是{self.gender},{msg}')

#定义了一个Student类，继承了一个Person类
class Student(Person):
    def __init__(self,name,age,gender,stu_id,grade):
        #对父类属性的初始化
        #第一种
        # super().__init__(name,age,gender)

        #第二种
        Person.__init__(self,name,age,gender)
        #Student类独有的属性
        self.stu_id = stu_id
        self.grade = grade
    def study(self):
        print(f'我叫{self.name},我今年{self.age},我是{self.gender}')

    def speak(self, msg):
        super().speak(msg)
        print(f'我是Student:我叫{self.name},我今年{self.age},我是{self.gender},{msg}')
# 创建Student类的实例对象
s1 = Student('玉鹏',18,'男生',260302,85)
p1 = Person('水哥',20,'男生')

s1.speak('哈喽')
# p1.speak('哈喽')#1自身实例 2Person
# isinstance(obj,Class):判断对象是否为指定类或其子类的实例
print(isinstance(s1,Person))
print(isinstance(p1,Person))
print(isinstance(s1,Student))
print(isinstance(p1,Student))
# issubclass(sub,supper):判断一个类是否为另外一个类的子类
print(issubclass(Person,Student))
print(issubclass(Student,Person))
