#!/usr/bin/python
# _*_ coding=utf-8 _*_

def search(array,number):
    left = 0
    right = len(array) - 1
    while(left < right):
         mid = (left + right) / 2
	 if array[mid] < number:
	      left = mid + 1
	 elif array[mid] > number:
	      right = mid - 1
	 else:
	      return mid
    return -1
if __name__ == "__main__":
  a = input("请输入一个列表:")
  b = input("请输入你要查找的值:")
  a.sort()
  print search(a,b)

       
       
    
