#!/usr/bin/python
# _*_ coding=utf-8 _*_
#从键盘输入一些字符串，逐个把他们送到磁盘上去，直到输入一个'#'为止

if __name__ == '__main__':
   from sys import stdout
   filename = raw_input('input a file name:\n')
   fp = open(filename,'w')
   ch = raw_input('input string:\n')
   while ch != '#':
         fp.write(ch)
	 stdout.write(ch)
	 ch = raw_input(' ')
   fp.close()
