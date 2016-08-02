#!/usr/bin/python
# _*_ coding=utf-8 _*_
#有两个磁盘文件A和B，各存放一行字母，要求把这两个文件中的信息合并(按字母顺序排列)，输出##到C文件中

if __name__ == '__main__':
   import string
   fp = open(r'/usr/src/Summer-study-program/python代码/test1.txt')
   a = fp.read()
   fp.close()

   fp = open(r'/usr/src/Summer-study-program/python代码/test2.txt')
   b = fp.read()
   fp.close()

   fp = open(r'/usr/src/Summer-study-program/python代码/test3.txt','w')
   l = list(a + b)
   l.sort()
   s = ' '
   s = s.join(l)
   fp.write(s)
   fp.close

