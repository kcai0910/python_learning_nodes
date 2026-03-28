class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #自定义方法
    #speak方法收到的参数是调用speak方法的实例对象，其他参数
    def speak(self,msg):
        print(f'我是{self.name},我今年{self.age},我是{self.gender},我想说{msg}')

p1 = Person('阿杰',18,'男')
p2 = Person('玉鹏',20,'男')
p3 = Person('超然',21,'女')
print(Person.__dict__)
# 可以验证实例身上没有speak方法
print(p1.__dict__)
#通过Person类创建的实例对象都可以调用speak方法
p1.speak('我想打麻将')
p3.speak('吃东西')

#如果实例身上有方法，就执行自身的，如果没有就找类
#查找过程1：实例对象自身  2：实例的创造者（类）
def speak(msg):
    print(f'我是外侧函数,我想说{msg}')
p1.speak = speak
p1.hobby = '打球'
print(p1.__dict__)
print(p1)
print(p2.__dict__)
print(Person.__dict__)
p1.speak('你好')
p2.speak('999')