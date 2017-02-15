#pillow
from PIL import Image
im=Image.open('./image/litten.png')
print(im.format,im.size,im.mode);

im.thumbnail((100,100));
im.save('./image/thumb.jpg',"JPEG");


#class说明：
#要初始化的对象必有__init__函数
#class里面的方法都有self参数
class Student(object):
	"""docstring fos Student"""
	def __init__(self, name,score):
		self.name=name
		self.score=score

	def print_score(self):
		print("%s\'s score is %s." % (self.name,self.score))

bob=Student("Bob",82);
Alice=Student("Alice",94);
bob.print_score();
Alice.print_score();		


#外部函数也可以输出对象的属性值
#eg:
def print_std(std):
	print("%s\'s score is %s." % (std.name,std.score))
print(print_std(bob));
print(print_std(Alice));

#Python允许对实例变量绑定任何数据
bob.age=20;
print(bob.age);
#print(Alice.age);Error
#
#
#
##class说明：
#必有__init__函数
#class里面的方法都有self参数
class Student(object):
	"""docstring fos Student"""
	def __init__(self, name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print("%s\'s score is %s." % (self.__name,self.__score))

	def getname(self):
		return self.__name;

bob=Student("Bob",82);
Alice=Student("Alice",94);
bob.print_score();
Alice.print_score();
#print(bob.__name);#私有变量不可访问
print(bob._Student__name);#但是通过_Student__name来访问

bob.__name="Charis";#这种方式不能改变对象的name
print(bob.getname());
'''
附上一段666的评论：
在一个实例里，
__girl表示“我是贞女，你不能上我”
_girl表示“你虽然可以上我，但你应该把我看做贞女”
girl表示“我是荡妇，谁都可以上我”
但是python仍然可以用_实例名__girl强上贞女
……
'''


#继承
#
#

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print("Animal is running....");


class Dog(Animal):
	"""docstring for Animal"""
   
	def run(self):
		print("Dog is running...")
animal=Animal();
dog=Dog();
dog.run();

#判断变量是否是某一个类型
print(isinstance(dog,Dog));
print(type(dog))

def run_twice(animal):
	#animal.run();
	animal.run();

run_twice(animal);
run_twice(dog);

#传入Animal或者其子类不是必须的
class Timer(object):
    def run(self):
        print('Start...')

timer=Timer();
run_twice(timer);

class Teacher(object):
	name="Teacher"
	"""docstring for Teacher"""
obj=Teacher();
print(obj.name);

obj.name="Pony";
print(obj.name);
print(Teacher.name);
del obj.name
print(obj.name);


#获取对象的信息：
#type 判断对象类型
print(type(123));

import types
def fn():
	pass

print(type(fn))
#instance，
print(isinstance([1, 2, 3], (list, tuple)));

#dir
print(dir('ABC'));#所有属性和方法
print(len("ABC"));
#等价于
print("ABC".__len__());

#getattr,setattr,hasattr
#test:
class Test(object):
	"""docstring for Test"""
	def __init__(self):
		self.name = "test"

obj=Test();
print(hasattr(obj,"name"));
setattr(obj,"score",90);
print(obj.score);
print(getattr(obj,"score",80))


