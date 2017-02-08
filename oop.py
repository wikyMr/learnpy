#class说明：
#必有__init__函数
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