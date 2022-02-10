class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，我现在{1}岁了'.format(self.name,self.age)

stu1=Student("张三",15)
print(stu1,id(stu1))
print(Student.__dict__)