import os
import re
import requests


class video:
    url = "http://www.dalisc.com/guochanju/nishiwoderongyao/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    def get_url(self):#请求主页面链接
        response1 = requests.get(self.url, headers=self.headers)  # 请求剧集网页
        response1.encoding = 'utf-8'
        t1 = '<a target="_blank" href="(.*?)">'
        result1 = re.findall(t1, response1.text)
        return result1

    def get_url2(self):#请求剧集链接
        list_url=self.get_url()
        m3u8_list = []
        for i in list_url:
            response1 = requests.get("http://www.dalisc.com"+i, headers=self.headers)  # 请求剧集网页
            #print(response1.text)
            t1 = '"url":"(.*?)"'
            result1 = re.findall(t1, response1.text)
            for m3u8 in result1:
                m3u8=m3u8.replace("\\","")
                m3u8_list.append(m3u8)
        return m3u8_list

    def get_url3(self):#请求保存m3u8链接的文本
        pass





if __name__ == '__main__':
    vi = video()
    vi.get_url2()