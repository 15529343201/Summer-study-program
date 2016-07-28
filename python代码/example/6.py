#!/usr/bin/python
# _*_ coding=utf-8 _*_

def power1(x,n):
    result = 1
    for i in range(n):
        result *= x 
    return result

def power2(x,n):
    if n == 0:
       return 1
    else:
       return x * power2(x,n-1)

m = input('请输入x和n的值(以逗号隔开):')
x,n = m

print power1(x,n)
print power2(x,n)


