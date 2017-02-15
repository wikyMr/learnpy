#限制实例属性
"-slots-"
#eg:
class Student(object):
	"""docstring for Student"""
	__slots__=("name","score");
	pass
bob=Student();
bob.name="Bob";
bob.score=80;
#bob.age=20;#error
class graduateStudent(Student):
	pass
#对继承的实例不起作用
Alice=graduateStudent();
Alice.score=100;
print(Alice.score);
#在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

#设置属性的读写操作
class Teacher(object):
	"""docstring for Teacher"""
	@property
	def birth(self):
		return self._birth;
	@birth.setter
	def birth(self,value):
	 	self._birth=value;
	@property
	def age(self):
		return 2017-self.birth;

t=Teacher();
t.birth=1995;#可设置
print(t.birth);
#t.age=10;
print(t.age);

#homework:

class Screen(object):
	"""docstring for Screen"""
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError("必须为整数")
		if value<0:
		    raise ValueError("必须为非负数")
		self._width=value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError("必须为整数")
		if value<0:
		    raise ValueError("必须为非负数")
		self._height=value
	@property
	def resolutions(self):
		return self._width*self._height;

screen=Screen();
screen.width=100
screen.height=120
print(screen.resolutions);
#print(dir(screen));

#Mixlin
#多重继承
class Father(object):
	"""docstring for Person"""
	pass
	def run(self):
		print("Father is running...")
class Mother(object):
	"""docstring for Person"""
	pass
	def run(self):
		print("Mother is running...")
class Me(Father,Mother):
	"""docstring for Person"""
	pass

me=Me();
me.run();

#定制类
class ClassMate(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	def __str__(self):#定制返回类的信息，面向用户
		return "Classmate:%s"% self.name;
	__repr__=__str__;#面向开发者,python cmd敲击a输出的信息
s=ClassMate("Bob");
print(s);
print("%r" % s);

#迭代
class Classmates(object):
	"""docstring for Fb"""
	def __init__(self):
		self.n=0;
		self.n2=0
	def __iter__(self):#返回迭代的对象
		return self
	def __next__(self):
		self.n2=self.n*self.n
		self.n=self.n+1;
		if(self.n>10):
			raise StopIteration()
		return self.n2
	def __getitem__(self,n):
		if isinstance(n,int):#返回单个元素
			if 0<=n<=10:
				return (n)*(n);
			if n>10:
				raise "Can't found the number."
			if n<0:
				pass		
		if isinstance(n,slice):#返回多个元素
			pass
cs=Classmates()
'''
for x in cs:#这里不断的调用next()来输出n
	print(x);
	pass
'''
#cs类似于list，但是却不能输出
print(cs[5]);#这个会出错，怎么实现呢
#print(cs[5:10]);#这里又会出错了
#
#错误处理
'''
def div(_div):
	return 10/_div;
def div2(m):
	return div(m)*10;
def main():
	print(div2(0));
main();
'''
#1.记录错误继续执行
'''
import logging
def div(_div):
	return 10/_div;
def div2(m):
		return div(m)*10;

def main():
	try:
		div2(0)
	except Exception as e:
		logging.exception(e)

print(main());
print("END");#可以继续执行
'''
#2.多层函数调用抛出异常
def div(_div):
	if _div==0:
		raise ValueError("invalid values:%s"% _div);
	return 10/_div;
def div2(m):
		try:
			div(m)*10;
		except Exception as e:
			print("Value error.")
			raise
def main():
	div2(0)

print(main());
print("END");#可以继续执行


