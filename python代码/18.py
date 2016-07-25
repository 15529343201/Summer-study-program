#!/usr/bin/python
# _*_ coding=utf-8 _*_

#求s=a+aa+aaa+aaaa+aaaaa的值，其中a是一个数字

Tn = 0
Sn = []
n = int(raw_input('n = :\n'))
a = int(raw_input('a = :\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y : x + y,Sn)
print Sn
