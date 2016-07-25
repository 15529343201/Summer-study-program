#!/usr/bin/python
# _*_ coding: UTF-8 _*_
#一个整数，它加上100和268都是一个完全平方数，请问该数是多少?

import math
for i in range(10000):
    #转换成整形值
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100)and(y*y==i+268):
          print i
