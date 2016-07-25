#!/usr/bin/python
# _*_ coding=utf-8 _*_

#将一个正整数分解质因数，例如：90=2×3×3×5
'''对n进行分解质因数，应先找到一个最小的质数k,
   (1)如果这个指数恰好等于n，则说明分解质因数的过程已结束，打印出即可
   (2)如果n<>k,但n能被k整除，则应打印出k的值，并用n除以k的商，作为新的正整数       n，重复执行第一步
   (3)如果n不能被k整除，则用k+1作为k的值，重复执行第一步
'''

from sys import stdout
n = int(raw_input("input number:\n"))
print "n = %d" % n

for i in range(2,n+1):
    while n != i:
          if n % i == 0:
	     stdout.write(str(i))
	     stdout.write("*")
	     n = n / i
	  else:
	     break
print "%d" % n
