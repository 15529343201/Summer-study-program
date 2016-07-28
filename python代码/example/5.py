#!/usr/bin/python
# _*_ coding=utf-8 _*_

def factorial1(n):
    result = n
    for i in range(1,n):
          result *= i
    return result

def factorial2(n):
    if n == 1:
       return 1
    else:
       return n*factorial2(n-1)

n = int(raw_input('x='))

print factorial1(n)
print factorial2(n)


