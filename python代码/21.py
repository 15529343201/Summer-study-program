#!/usr/bin/python
# _*_ coding=utf-8 _*_
#计算字符串中字串出现的次数

if __name__ == '__main__':
   str1 = raw_input('input a sring:\n')
   str2 = raw_input('input a sub string:\n')
   ncount = str1.count(str2)
   print ncount
