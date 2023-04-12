'''回调函数：简单来说就是定义一个函数，然后将这个函数的函数名传递给另一个函数做参数，以这个参数命名的函数就是回调函数。'''
def my_callbcak(args):
    print(*args)

def caller(args, func):
    func(args)

caller((1,2), my_callbcak)


'''递归函数的定义 : 自己调用自己的函数就是递归'''
def digui(n):
    print(n,"<====1===>")
    if n > 0:
        digui(n-1)
    print(n,"<====2===>")
digui(5)

'''闭包函数：在一个函数内返回了一个内函数， 并且这个返回的内函数还使用了外函数中的局部变量，就是闭包函数。'''
def outer(a):  #outer是外函数
    def inner(b):  # inner是内函数
        print(a + b)  # 在内函数中用到了外函数临时变量
    return inner  # 外函数的返回值是内函数的引用
res = outer(5)  # res = inner
res(10)  # 15，res存了外函数的返回值，也就是内函数的引用，这里相当于执行inner函数

'''在python中使用lambda表达式来定义匿名函数'''
# 普通函数
def sum(x,y):
    return x+y
print(sum(2,3))   #返回5
# 改成lambda表达式来封装
res = lambda x,y:x+y
print(res(2,3))
