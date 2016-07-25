#!/usr/bin/python
# _*_ coding=utf-8 _*_

#判断100-200之间有多少个素数，并输出所有素数

h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(100,201):
    k = int(sqrt(m))
    for i in range(2,k+1):
        if m%i == 0:
	   leap = 0
	   break
    if leap == 1:
        print '%-4d' % m,
	h += 1
	if h % 10 == 0:
	   print ' '
    leap = 1
print '\nThe total is %d' % h
