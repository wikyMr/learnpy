#迭代
#迭代dict
d={"Tomi":90,"Bobi":80,"Huvy":75}
#遍历数值：
for key in d.keys():
	pass
	#print(key);
for value in d.values():
	pass
	#print(value);
for key,value in d.items():
	pass
	#print(key,":",value);
#判断是否为可迭代对象：
from collections import Iterable
#print(isinstance([1,2,3],Iterable));

#把下标也输出来：
for i,value in enumerate(['a','b','c']):
#	print(i,value);
	pass

#yield不是很懂
'''
def h():
    print 'Wen Chuan'
    yield 5
    print 'Fighting!'
c = h()
c.next()

#yield
def g():
	print("1");
	yield 1
	print("hello");
	yield 2
	yield 3
#print(isinstance(g(),Iterable));
c=g();
c.next();
it=iter([1,2,3,4]);
print(next(it));
'''

#List Comprehensions
#生成1，4,9,16
#法一：
L=[];
for x in range(1,10):
	L.append(x*x);

for y in L:
	pass
	#print(y);

#法二：
L=[x*x for x in range(1,11)];
L=[x*x for x in range(1,11) if x%2==0];#4,16,36,64,100
for y in L:
	pass
	#print(y);

#列出目录下的所有的文件
import os
L=[d for d in os.listdir('.')];
for y in L:
	pass
	#print(y);
#遍历：
d={"a":20,"b":30,"c":40};
L=[k+':'+str(v) for k,v in d.items()];
print(L);
L=['Hello','Python'];
l=[s.lower() for s in L];
print(l);

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)];
print(L2);

#迭代器
def fib():
	yield 1
	yield 2
	yield 3 
g=fib();
while True:
	try:
		x=next(g)
		print(x)
	except StopIteration as e:
		#print(e.value)
		break

#何为迭代器
#直接作用于for循环的对象统称为可迭代对象：Iterable:
#1.集合数据类型：list,tuple,dict,set,str;
#2.生成器和带yield的generator function

#判断
from collections import Iterable,Iterator
print(isinstance('str',Iterable));

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#iterable变成iterator:
print(isinstance([],Iterator));#False
print(isinstance(iter([]),Iterator))

#高阶函数
from functools import reduce
def fn(x,y):
	return x*10+y;
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];
print(list(map(char2num,"1357")));
print(reduce(fn,list(map(char2num,"1357"))));

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。

#filter()
#过滤非回数
def is_palindrom(n):
	return str(n)==str(n)[::-1];
output=filter(is_palindrom,range(1,10));
print(list(output));

#函数返回：
def lazy_sun(*args):
	def sum():
		s=0
		for x in args:
			s=s+x;
		return s;
	return sum
f=lazy_sun(1,3,5,7);
print(f());


#匿名函数
L=list(map(lambda x:x*x,[1,2,3,4,5]));
print(L);

#装饰器decorator
def now():
	print('2017-2-7');

f=now;
f();

#装饰器部分
#得到函数名
print(now.__name__);

def log(func):
	def printlog():
		print('Call %s()'%func.__name__)
	return printlog;

@log
def now1():
	print('2017-2-7');

print(now1());
print(now1.__name__);#函数名已经改变了

'''
def log2(func):
	def printlogs():
		print("begin call")
		def printlog2():
			print('Call %s()'%func.__name__)
		return printlog2
    	print("begincall")
    return printlogs

@log2
def now2():
	print('2017-2-7');

print(now2());
print(now2.__name__);#函数名已经改变了
'''

#偏函数
import functools
int2=functools.partial(int,base=2)

#x相当于
def int3(x,base=2):
	return int(x,base);

print(int2('1000'));
print(int3('1000'));