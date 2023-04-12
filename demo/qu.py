import queue

# 先入先出(默认)
q = queue.Queue(maxsize=2)
q.put(1)
q.put(2)
#q.put(3,block=False)
print(q.get())
print(q.get())
q.task_done()
q.join()
q.task_done()


#
# print(q.get(block=False))

# 1
# 2
# 3
# 先入后出
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
# # 输出
# # 3
# # 2
# # 1
#
# # 数据可设置优先级，同优先级按照ASCII排序
# q = queue.PriorityQueue()
# # 本次写入元素为元组
# q.put((2, '2'))
# q.put((1, '1'))
# q.put((3, '3'))
# q.put((1, 'a'))
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# # 输出
# # (1, '1')
# # (1, 'a')
# # (2, '2')
# # (3, '3')