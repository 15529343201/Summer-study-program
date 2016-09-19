#-*- coding:utf-8 -*-  
import sys 
import os 
import string 
import re 
from datetime import datetime 
  
QUIT_FLAG = False
ADDRS_LIST = "addr_list.txt"
_addrs_dict = {}  
_addrs_count = 0
DEBUG=2
def info(message): 
  global DEBUG 
  if DEBUG > 0: 
    print message 
  
def debug(message): 
  global DEBUG 
  if DEBUG > 1: 
    print message 
  
def warn(message): 
  global DEBUG 
  if DEBUG > 0: 
    print message 
    
def error(message): 
  print message 
  
def help(): 
  print "用法：输入菜单中的命令即可执行相应操作！"
  print "可用菜单命令如下："
  showMenu() 
  
def showMenu(): 
  print "+******************操作菜单***********************+"
  print "|查看所有联系人(all) | 查找联系人(find)      |"
  print "|添加联系人(add)   | 删除联系人(remove)     |"
  print "|编辑联系人(edit)  | 保存并退出(save)      |"
  print "|使用帮助(help)   | 退出但不保存(quit)     |"
  print "+_________________________________________________+"
  
def showError(info): 
  print info 
  
  
def doSwitch(op): 
  if op == "all": 
    doAll() 
  elif op == "find": 
    doFind() 
  elif op == "add": 
    doAdd() 
  elif op == "remove": 
    doRemove() 
  elif op == "edit": 
    doEdit() 
  elif op == "save": 
    doSave() 
  elif op == "help": 
    help() 
  elif op == "quit": 
    doQuit() 
  else: 
    showError("错误：您输入的命令有误，请重新输入。需要帮助请输入help！") 
  
def verifyInput(items): 
  _flag = True
  _rPhone = re.compile(r'1[0-9]{10}') 
  _rQQ  = re.compile(r'[1-9][0-9]{4,9}') 
  if len(items[0]) > 10: 
    _flag = False
    print "姓名太长了！"
  if not _rPhone.match(items[1]): 
    _flag = False
    print "手机号码格式不正确"
  if not _rQQ.match(items[2]): 
    _flag = False
    print "QQ号码输入有误"
  return _flag 
    
  
def buildAddr(addr): 
  _addr={} 
  items=addr.split() 
  if len(items) < 3: 
    print "您输入的信息太少了"
    return None
  if not verifyInput(items): 
    return None
  
  _addr['name']=items[0] 
  _addr['phone'] = items[1] 
  _addr['QQ'] = items[2] 
  return _addr 
  
def addAddr(addr): 
  global _addrs_count,_addrs_dict 
  _addrs_count+=1
  _addr=buildAddr(addr) 
  if not _addr: 
    return None
  _addrs_dict[_addrs_count]=_addr 
  
def init(): 
  if not os.path.isfile(ADDRS_LIST): 
    return None
  
  faddr=open(ADDRS_LIST,"r") 
  for line in faddr:  
    if len(line) == 0: 
      continue
    addAddr(line) 
  faddr.close() 
  
  
def save(): 
  global _addrs_dict 
  faddr=open(ADDRS_LIST,"w+") 
  for addr in _addrs_dict.values(): 
    faddr.write("{0}\t{1}\t{2}\n".format(addr['name'],addr['phone'],addr['QQ'])) 
  faddr.flush() 
  faddr.close() 
  
  
def doAll(): 
  global _addrs_dict 
  if len(_addrs_dict) < 1: 
    print "联系人当中暂无记录！"
    return None
  printHead() 
  for key,addr in _addrs_dict.items(): 
    printAddr(key,addr) 
  
def doFind(): 
  _flag=False
  flag1=flag2=flag3=False
  cond=raw_input("请输入查询信息：>") 
  debug("DEBUG:{0}".format(cond)) 
  if len(cond) == 0: 
    return None
  if cond.isdigit(): 
    flag1=findById(int(cond,10)) 
    flag2=findByPhone(cond) 
    flag3=findByQQ(cond) 
  else: 
    flag1=findByName(cond) 
    
  _flag = flag1 or flag2 or flag3  
  if not _flag: 
    print "没有查找到任何联系人！"
  
def doAdd(): 
  line = raw_input("请依次输入联系人的姓名，手机号码，QQ号码>") 
  if len(line) == 0: 
    return None
  addAddr(line)   
  
def existsId(_id): 
  global _addrs_dict 
  return _addrs_dict.has_key(_id) 
#  if _id > _addrs_count or _id < 1: 
#    return False  
#  else: 
#    return True 
  
def doRemove(): 
  FLAG = True
  while FLAG: 
    key=raw_input("请输入要删除的联系人的编号(取消请输入#）") 
    if key == '#': 
      FLAG = False
      continue
    if not existsId(int(key,10)): 
      print "不存在您所输入编号的联系人。请确认"
      continue
    
    print "编号为 {0} 的联系人信息如下：".format(key) 
    printById(int(key,10)) 
    yesOrNo=raw_input("您确定要删除上述联系人吗？(y/n)") 
    if yesOrNo in "yY": 
      removeById(int(key,10)) 
      print "删除成功！"
    yesOrNo=raw_input("您还需要继续删除联系人吗？(y/n)") 
    if not yesOrNo in "yY": 
      FLAG = False
  
  
  
def doEdit(): 
  FLAG = True
  while FLAG: 
    key=raw_input("请输入要编辑的联系人的编号(取消请输入#）") 
    print "DEBUG:key:{0}".format(key) 
    if key == '#': 
      FLAG = False
      continue
    if not existsId(int(key,10)): 
      print "不存在您所输入编号的联系人。请确认"
      continue
    
    print "编号为 {0} 的联系人信息如下：".format(key) 
    printById(int(key,10)) 
    updateById(int(key,10)) 
    FLAG = False
  
  
def doSave(): 
  save() 
  doQuit() 
  
def doQuit(): 
  global QUIT_FLAG 
  QUIT_FLAG = True
  print "正在退出……"
#  exit(0) 
  
def printHead(): 
  print "+-----+----------+---------------+---------------+"
  print "|编号 |  姓名  | 手机号码   |   QQ号码  |"
  print "+-----+----------+---------------+---------------+"
  
def printAddr(key,addr): 
#  print "+-----+----------+---------------+---------------+" 
  print "|{0:^5}|{1:^10}|{2:^15}|{3:^15}|".format(key,addr['name'],addr['phone'],addr['QQ']) 
  print "+-----+----------+---------------+---------------+"
  
  
  
def printById(_id): 
  global _addrs_dict 
  printHead() 
  printAddr(_id,_addrs_dict[_id]) 
  
def removeById(_id): 
  global _addrs_dict 
  _addrs_dict.pop(_id) 
  
def updateById(_id): 
  global _addrs_dict 
  _addr= _addrs_dict.get(_id) 
  
  print "请输入该联系人的新信息，相应留空则保留原有信息"
  name=raw_input("请输入新姓名：>") 
  if len(name) > 0: 
    _addr['name']=name 
  
  phone=raw_input("请输入新手机号码：>") 
  if len(phone) > 0: 
    _addr['phone']=phone 
  
  qq=raw_input("请输入新的QQ号码：>") 
  if len(qq) > 0 : 
    _addr['QQ']=qq 
  
  _addrs_dict[_id]=_addr 
  print "更新成功！"
  print "联系人新的信息如下："
  printById(_id) 
  
def findById(_id): 
  if existsId(_id): 
    printById(_id) 
    return True
  else: 
    return False
  
def findByField(cond,field='name'): 
  global _addrs_dict 
  _flag = False
  for key,addr in _addrs_dict.items(): 
    if addr[field].find(cond) != -1: 
      printAddr(key,addr) 
      _flag=True
  return _flag 
  
def findByName(name): 
  return findByField(name,'name') 
  
def findByPhone(phone): 
  return findByField(phone,'phone') 
  
def findByQQ(qq): 
  return findByField(qq,'QQ') 
  
  
  
def main(): 
  init() 
  showMenu() 
  while(not QUIT_FLAG): 
    operation=raw_input("请在此处输入菜单命令>") 
    doSwitch(operation) 
  
  
if __name__=='__main__': 
  main() 

