import datetime
import os
import time
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool

import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(BASE_DIR+"/data/img_url.txt") as f:
    url_list=f.read().splitlines()


def get_url(url):
    response = requests.get(url)
    nowtime = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    print(nowtime)
    with open(BASE_DIR + '/data/picture' + '/' + nowtime + '.jpg', mode='wb') as file:
        file.write(response.content)
pool=Pool(10)
result=pool.map(get_url, url_list)

