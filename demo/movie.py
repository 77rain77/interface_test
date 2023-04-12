import os
import re
import requests
import threading


class Movie:
    url="https://www.wangci.net/dongman/qyqx/"
    def movie(self):
        global headers
        headers = {
            "referer": "https://www.wangci.net/dongman/qyqx/",  # 防盗链
            "user - agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 103.0.0.0Safari / 537.36",
        }
        response1 = requests.get(self.url, headers=headers)  # 请求主页面
        print(response1.text)
        response1.encoding = 'utf-8'
        t1='<a title="(.*?)" href="(.*?)" target="_blank">'
        result1 = re.findall(t1, response1.text)
        for mv in result1: #对电影名字做数据剔除
            global mv_list
            mv_list = list(mv)
            res=re.search(r"[0-9][0-9]|[0-9]",mv_list[0])
            if res:
                mv_list[0]=res.group(0)
            if "在线播放" in mv_list[0]:
                mv_list[0]=mv_list[0][:-4]
            response2= requests.get("https://www.wangci.net"+mv[1], headers=headers) #请求电影链接
            self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目根目录
            t2='"url":"(.*?)",'
            result2 = re.findall(t2, response2.text)
            for m3u8 in result2:
                m3u8=m3u8.replace("\\","")#去除链接多余的\
                response3=requests.get(m3u8, headers=headers) #请求存m3u8目录的文本链接
                print(response3.text)
                t3="/(.*?).m3u8"
                result3=re.findall(t3, response3.text)
                self.response4= requests.get("https://cdn.zoubuting.com/"+ result3[0] +".m3u8", headers=headers)
                all = re.findall("https:(.*?).ts", self.response4.text) #请求视频流链接
                for i in all:
                    with open(self.BASE_DIR + "/data/movie/"+mv_list[0]+".mp4", mode='ab') as f:
                        videoContent = requests.get("https:"+i+".ts", headers=headers).content
                        f.write(videoContent) #存放视频
                        print(i)

#     def montagef(self):
#         all = re.findall("https:(.*?).ts", self.response4.text)  # 请求视频流链接
#         for i in all:
#             with open(self.BASE_DIR + "/data/movie/" + mv_list[0] + ".mp4", mode='ab') as f:
#                 videoContent = requests.get("https:" + i + ".ts", headers=headers).content
#                 f.write(videoContent)  # 存放视频
#                 print(i)
#
#
#
if __name__ == '__main__':
    mv=Movie()
    mv.movie()
    # for i in range(50):
    #     thead = threading.Thread(target=mv.montagef, )
    #     thead.start()
    #     thead.join()

