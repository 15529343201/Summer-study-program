#!/usr/bin/python
# _*_ coding=utf-8 _*_

# 利用条件运算符的嵌套来完成此题:学习成绩>=90分的同学用A表示，60-89分之间的## 用B表示，60分以下用C表示

score = int(raw_input('input score:\n'))
if score >= 90:
   grade = 'A'
elif score >= 60:
   grade = 'B'
else:
   grade = 'C'

print '%d belongs to %s' % (score,grade)


