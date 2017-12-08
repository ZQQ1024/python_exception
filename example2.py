# encoding=UTF8
#python异常，例子2
#exception捕获异常种类、顺序

try:
    a = 10
    b = 0
    a/b

    dic={}
    dic[1]=1
    print dic[2]
except KeyError , e:
    print e.message
except (Exception,SyntaxError) as e:
    #print "other exception!"
    print e.message
else:
    print "normally,else run!" #
#finally，不管异常与否，都会执行的
finally:
    print "mo matter whether or not,always run finally!" #异常必须捕获到，不捕获到程序就停了

#try出错后，后面的代码就不会运行了，层级相同也就只能又一个异常
#多个except，说明了捕获异常的顺序（Exception 捕获所有）和种类
#所有的except都没捕获到，程序异常结束，也就没finally什么事情了