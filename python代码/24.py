#!/usr/bin/python
# _*_ coding=utf-8 _*_

if __name__ == '__main__':
   import time
   start = time.time()
   for i in range(100):
       print i
   end = time.time()
   print end - start
