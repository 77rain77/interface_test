import os


def x(func):
    def m():
        func()
        print("18")
    return m
@x
def a():
    print("今天天气真好")
a()
'''将方法a传给x中func参数'''



def x(func):
    def m(*args,**kwargs):
        print(args)
        print(kwargs)
        func(args,kwargs)
    return m
@x
def a(para1,para2):
    print("真厉害")
    print(para1,para2)
a("RAIN","18",RAIN="年轻",R="貌美")
'''将a中的para1,para2传给args,kwargs'''


def u(name):
    def x(func):
        def m(*args, **kwargs):
            print(args)
            print(kwargs)
            func(args, kwargs)
            print(name)
        return m
    return x

@u("大大的")
def a(para1,para2):
    print("真厉害")
    print(para1,para2)
a("RAIN","18",RAIN="年轻",R="貌美")
'''将”大大的“传给name'''