import os
import re


class Util:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def open_text(self):
        with open (self.BASE_DIR+"/script_text/天选之子.txt",encoding='utf-8') as f:
            result=f.read().splitlines()
            text1=[]#剧本问答
            text2=[]#剧本提问
            text3=[]#回复例子
            text4=[]#剧本回复方向

            for i in result:
                if not i.__eq__(""):
                    text1.append(i)
            for index, value in enumerate(text1):
                if text1[index].startswith("【") :
                    text1[index-1]=text1[index-1]+text1[index]
                    text1.remove(text1[index])
                    for index, value in enumerate(text1):
                        if text1[index].startswith("【"):
                            text1[index - 1] = text1[index - 1] + text1[index]
                            text1.remove(text1[index])

            for i in text1:
                if re.search(r"{\d+-\d+}", i):
                    pattern = r'【.*?】|<br>|☛.*?☚'
                    i = re.sub(pattern, '', i)
                    text2.append(i)
                elif re.search(r"{\d+-\d+-\d+}", i):
                    pattern = r'【.*?】|<br>|☛.*?☚'
                    i = re.sub(pattern, '', i)
                    text3.append(i)
                elif re.search(r"\[\d+-\d+-\d+]", i):
                    pattern = r'【.*?】|<br>|☛.*?☚'
                    i = re.sub(pattern, '', i)
                    text4.append(i)
            zipped = list(zip(text3, text4))

            # print(text1)
            # print(text2)
            # print(text3)
            # print(text4)
            #print(zipped)
            return text2,text3,text4,zipped

if __name__ == '__main__':
    Util().open_text()


