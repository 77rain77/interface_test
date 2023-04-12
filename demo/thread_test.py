import time
from threading import Thread, current_thread


def target():
    if current_thread().name == "1":
        time.sleep(5)
    else:
        time.sleep(4)
    print("线程{}已退出".format(current_thread().name))

if __name__ == '__main__':
    thread01 = Thread(target=target,daemon=True,name="1")  # 参数timeout可以用来设置主线程陷入阻塞的时间，如果线程不是守护线程，即没有设置daemon为True，那么参数timeouttimeout 是无效的，主线程会一直阻塞，直到子线程执行结束。
    thread02 = Thread(target=target,daemon=True,name="2")
    thread01.start()
    thread02.start()
    thread01.join()
    # print("程序因线程1陷入阻塞")
    # thread01.join(timeout=3)
    # print("程序因线程2陷入阻塞")
    # thread02.join(timeout=3)
    print("主线程已退出")

