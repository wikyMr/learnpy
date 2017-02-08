#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv#hello
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


print(__name__);
print(__doc__);
if __name__=='__main__':
    test()

#模板的特殊变量：
#1.__author__
#2.__name__,当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
#3.__doc__,所有的注释
#_x或者__x为private变量；