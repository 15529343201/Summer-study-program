#!/usr/bin/python
# _*_ coding=utf-8 _*_

if __name__ == '__main__':
   import time
   start = time.clock()
   for i in range(100):
       print i
   end = time.clock()
   print end - start
