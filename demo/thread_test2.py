import time
import requests
from multiprocessing.dummy import Pool

# 自定义函数
def query(url):
    requests.get(url)

start = time.time()
for i in range(100):
    query('https://www.csdn.net/')
end = time.time()
print(f'单线程循环访问100次CSDN，耗时：{end - start}')

start = time.time()
url_list = []
for i in range(100):
    url_list.append('https://www.csdn.net/')
pool = Pool(5)
pool.map(query, url_list)
end = time.time()
print(f'5线程访问100次CSDN，耗时：{end - start}')

