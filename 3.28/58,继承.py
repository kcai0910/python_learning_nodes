""""""
"""
继承:指的是一个类可以继承另一个类的属性和方法 
Person:父类，超类，基类
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
        print(f'我是Student:我叫{self.name},我今年{self.age},我是{self.gender},{msg}')
# 创建Student类的实例对象
s1 = Student('玉鹏',18,'男生',260302,85)
print(s1.__dict__)
#查看实例对象是被哪个类创建的
print(type(s1))
def speak(msg):
    print(msg)
# s1.speak = speak
s1.speak('你好')#1查找实例自身 2:Student类 3:Person类
