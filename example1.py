# encoding=UTF8
#python异常，例子1
#try,else,finally含义

try:
    a = 10
    b = 0
    a/b
except Exception as e: # Exception , e
    print "has exception!"
else:
    print "normally,else run!" #
finally:
    print "mo matter whether or not,always run finally!" #异常必须捕获到，不捕获到程序就停了

#try：可能出错的代码段
#except：那种错误
#else：try正常，执行的代码段
#finally：不论try是否出错，都执行的代码段