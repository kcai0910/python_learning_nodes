""""""
"""
方法重写：如果子类定义了与父类相同的方法，则子类会覆盖父类中的方法：重写

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