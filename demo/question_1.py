import datetime
from datetime import time
from threading import Thread


def test():
    for i in range(20):
        print(i)
time1=datetime.datetime.now()
for i in range(5):
    thread01 = Thread(target=test)
    thread01.start()
    thread01.join()
time2=datetime.datetime.now()
time=time2-time1
print("多线程使用时间",time)





# time1=datetime.datetime.now()
# for i in range(20):
#     print(i)
# time2=datetime.datetime.now()
# time=time2-time1
# print("单线程使用时间",time)

