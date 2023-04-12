# 1.导入包和模块
import multiprocessing
import time
import queue
from queue import PriorityQueue as pq


def sing():
    for i in range(3):
        print("i am sing ooo~")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("i am dance lll~")
        time.sleep(0.5)

def list():
    q = queue.Queue()  # 创建队列对象
    q.put(1)  # 队列尾部插入元素
    q.put(2)
    q.put(3)
    print(q.queue)  # 查看队列中的所有元素
    a = q.get()  # 返回并删除队列头部元素
    print(a)
    print(q.queue)  # 运行结果deque([2,3])

    lifoQueue = queue.LifoQueue()  # 创建对象
    lifoQueue.put(1)
    lifoQueue.put(2)
    lifoQueue.put(3)
    print(lifoQueue.queue)
    lifoQueue.get()  # 返回并删除队列尾部元素
    print(lifoQueue.queue)  # 运行结果[1,2]

    q = queue.LifoQueue(maxsize=5)
    # 优先级队列
    q = queue.PriorityQueue(maxsize=5)
    # 先进先出类型的简单队列，没有大小限制
    q = queue.SimpleQueue()

def test():
    str_ = '["a","b","c"]'
    str_=str(str_)
    print(str_)
    print(eval(str_)[0])
    print(str_[2:3])



if __name__ == '__main__':
    # 2.使用进程类创建进程对象
    # target ：指定进程执行的函数名，不加括号
    # sing_process = multiprocessing.Process(target=sing)
    # dance_process = multiprocessing.Process(target=dance)
    #
    # # 3. 使用进程对象启动进程执行指定任务
    # sing_process.start()
    # dance_process.start()
    #list()
    test()