'''判断语句
age1 = 15;
if age1>=18:
	print("adult")
else:
	print('not adult')
'''
#list
classmate=['a','b','c'];
#print(classmate[0]);#a
classmate.append("d");
#print(classmate[2]);

#tuple
mytuple=(1,);
#mytuple[0]=2;#error
#print(mytuple[0]);

#判断语句
'''
age=10;
if age >5:
	print("Older than 5.");
else:
	print("Yonger than 5.");

#input:
#s=input("input you birth:");
s="2";
birth=int(s);
if birth>=10:#birth为string类型的：
	print("Older.");
else:
	print("Yonger.");
'''
#for
sum=0;
for x in range(11):
	#print(x);
	sum+=x;
#print(sum);

#while:
n=0
sum=0
while n<100:
	sum+=n;
	n=n+1;
#print(sum);

#dict
d={"Bob":90,"Michael":80,"Tracy":95}

#print(d);
#print(d["Bob"]);
'''
if d.get("Bob"):
	print("Found.");
else:
	print("Not found.");

'''
#print("hello,word!");
#
#调用函数 invoking function
n1=250
#print(hex(n1));

#函数定义：
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad opetrand type')
	if x>=0:
		return x
	else:
		return -x

#print(my_abs(-3));

import math
def quadratic(a,b,c):
	r=b*b-4*a*c;
	if r>0:
		x1=(-b+math.sqrt(r))/(2*a)
		x2=(-b-math.sqrt(r))/(2*a)
		return x1,x2
	elif r==0:
			x= -b/(2*a)
			return x
	else:
		return '没有实根'


#print(quadratic(2,3,1));
#print(quadratic(1,3,-4));


#可变参数
def calc1(number):
	sum=0
	for x in number:
		sum=sum+x
	return sum
#print(calc([1,2,3]));
#多值返回
def calc2(*number):
	sum=0
	for x in number:
		sum=sum+x
	return sum
#print(calc2(1,2,3))
#print(calc2());
number=[1,2,4];
#print(calc2(*number));

#关键字
def person(name,age,**other):
	print("name:",name,"age:",age,"other:",other);

#print(person("梁海琪",10,city="zhuhai"));
extra={"city":"zhihai","job":"student"}
#print(person("lianghaiqi",20,**extra));

#命名关键字
def person2(name,age,*,city,job):
	print(name,age,city,job);

#print(person2("Jack",20,city='Biejing',job='student'));
#print(person2("ha",10,city="",job=""));
#传入不受限制的关键字：
#**kw（关键字参数），可以只传入必选参数
#可变参数：
#*number，可以把list或tuple的元素变成可变参数传入0到n个数值
#命名关键字参数：



#切片：
L=[1,2,3,4,5];
L=list(range(100));
print(L[0:8]);
print(L[::6]);#每5个取一个
print(L[:]);#复制数组
print(L[:5:10]);#这个就比较难懂了==

