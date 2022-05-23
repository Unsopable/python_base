# class Card():
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count

#     def save(self, nums):
#         self.count += nums

#     def get(self, nums):
#         self.count -= nums

#     def transport(self, account, nums):
#         self.count -= nums

#     def __str__(self):
#         return "账户名为{}，余额为{}".format(self.name, self.count)


# my_card = Card("王鹤鸣", 10000000)
# # print(my_card)
# my_card.save(10000)


# # print(my_card)


# ########################
# class Phone():
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def __str__(self):
#         return "手机品牌为{}，型号为{}".format(self.brand, self.model)

#     def __call__(self, *args, **kwargs):
#         print("手机正在打电话")


# my_phone = Phone("荣耀", "magic2")
# print(my_phone)  # 手机品牌为荣耀，型号为magic2
# my_phone()  # 手机正在打电话


# ##########私有属性
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def display(self):
#         print("名字：{}，年龄：{}".format(self.name, self.__age))

#     ####设置set方法和get方法，访问和修改私有属性
#     def setAge(self, age):
#         self.__age = age

#     def getAge(self):
#         return self.__age

#     ######使用propert装饰器来写私有属性
#     ##相当于get
#     @property
#     def age(self):
#         return self.__age
#     ##相当于set
#     @age.setter
#     def age(self,age):
#         self.__age = age


# student = Person('王鹤鸣',18)
# # print(student.getAge())##18
# # student.setAge(20)
# # print(student.getAge())#20
# print(student.age)##18
# student.age = 25
# print(student.age)##25

# class Student(Person):
#     def __init__(self, name, mark, age):
#         super().__init__(name, age)
#         self.mark = mark

#     def __str__(self):
#         return "姓名：{}，年龄{}，成绩{}".format(self.name, self.getAge(), self.mark)


# class Worker(Person):
#     def __init__(self, name, salary, age):
#         super(Worker, self).__init__(name, age)
#         self.salary = salary


# student = Student("王鹤鸣", 100, 20)
# # print(student.__age)##错误
# # print(student)  ##age = 20
# student.setAge(25)
# # print(student)  ##age = 25
# max_time = 2
# days = [2,2,2,2,2,2,1]
# days.reverse()
# i = days.index(max_time)
# print(7-i)

import copy


a = ([1,23,2],4,5)
print(a)
b = copy.copy(a)
print(b)
print(id(a),id(b))


c = copy.deepcopy(a)
print(id(c))
print(id(a[0]),id(c[0]))
