'''不使用set函数，如何便捷的实现对列表的去重:
list_ = [11, 22, 33, 11, 33, 44, 55]
去重 后结果:
list_ = [11, 22, 33, 44, 55]'''
list_ = [11, 22, 33, 11, 33, 44, 55]
print(set(list_))
res = []
[res.append(i) for i in list_ if i not in res]
print(res)
