#!/usr/bin/bash
# _*_ coding=utf-8 _*_
#输出9*9乘法口诀表

#左下三角格式输出九九乘法表
for i in range(1, 10):
  print
  for j in range(1, i+1):
    print "%d*%d=%d" % (i, j, i*j),

#一行代码打印
print('\n'.join([ ' '.join([ "%d*%d=%2s" %(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

