#!/usr/bin/python
<<<<<<< HEAD
# _*_ coding: UTF-8 _*_
#有1,2,3,4个数字，能组成多少个互不相同且无重复的三位数？都是多少？

for i in range(1,5):
    for j in range(1,5):
         for k in range(1,5):
	      if(i!=k)and(i!=j)and(j!=k):
	           print i,j,k
