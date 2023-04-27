import calendar
import datetime

import hashlib
import json
import time
import urllib.parse
#from datetime import datetime

import requests


class GPT:
    def time(self):
        a = "'{\"msg\":\"【晓悟】你可以说收藏某作品，比如：\\u201c收藏环球大富翁\\u201d，就不用担心下次找不到啦<br>\'"
        b = "'{\"msg\":\"【晓悟】你可以说收藏某作品，比如：\u201c收藏环球大富翁\u201d，就不用担心下次找不到啦<br>\'"
        #print(a.encode('utf-8').decode("unicode_escape"))
        print(a)
        print(b)
        #print(a.encode('utf-8').decode('utf-8'))

if __name__ == '__main__':
    GPT().time()
    #GPT().get_textresponse()
    #GPT().get_chatresponse()
