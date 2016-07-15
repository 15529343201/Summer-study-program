#!/usr/bin/python
<<<<<<< HEAD
# _*_ coding: UTF-8 _*_
#有1,2,3,4个数字，能组成多少个互不相同且无重复的三位数？都是多少？

for i in range(1,5):
    for j in range(1,5):
         for k in range(1,5):
	      if(i!=k)and(i!=j)and(j!=k):
	           print i,j,k
=======
#_*_ coding:utf-8 _*_

#有1,2,3,4个数字，能组成多少互不相同且无重复数字的三位数？都是多少？

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                print i,j,k
>>>>>>> 6335d4770f061eec7fab5c3f959f41a47afa85cd
