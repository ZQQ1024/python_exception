# encoding=UTF8
#python异常，例子4
#自定义异常类,搭配raise操作

#异常类定义
class  MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message = message

#抛出异常，捕获异常
try:
    raise MyException("my exception!")
except MyException as e:
    print e.message
