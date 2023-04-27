import datetime
import hashlib
import json
import re
import urllib.parse
import calendar
import requests
import time

from chatgpt.util import Util


class GPT:
    #time = datetime.datetime.now().microsecond


    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "App-Channel-Id": "XIAOWU",
        "Accept": "*/*",
        "User-Agent": "CentAssist/1.1.9 (iPhone; iOS 12.4.8; Scale/3.00)",
        "Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9",
        "Authorization": "Bearer 7eafc7d7-afb5-4781-b2a5-160f573897b4",
        "Content-Length": "252",

    }

    def get_textresponse(self,title="打开天选之子",new_session=True):

        header={
            "Conent-Type":"application/json",
            "Authorization": "Bearer d8741989-2cd6-44f1-9be3-e4b85d13c267",
            "User-Agent": "CentAssist/1.1.9 (iPhone; iOS 12.4.8; Scale/3.00)",
            "App-Channel-Id":"oppochildwatch-watch-sdk-test",
        }
        data={
            "msg":title,
            "new_session":new_session
        }
        response = requests.post("https://sdk-test.centaurstech.com/api/sdk/chat", headers=header,json=data)
        time.sleep(3)
        result = response.text.encode('utf-8').decode('utf-8')
        print(response.text)
        pattern = r'【.*?】|<br>|☛.*?☚'
        #msg = eval(response.json()["payload"].replace("null",""))["msg"]
        result = result.replace("\n", "").replace(r'"', "").replace('\\', "")
        res = re.search(r"msg:(.*?),", result)
        if res:
            result = res[0].replace("msg:", "").replace(",", "")
        result_text=re.sub(pattern, '', result)
        #print(result_text)
        return result_text

    def get_gptresponse(self,msg="再给我另外十句",new_session=True):
        ts = calendar.timegm(time.gmtime()) * 1000
        appsecret = "c47902cb4f2ee740aa47057d95aaa2db"
        uid = "Console.AutoTest.0.1_auto_test_" + str(ts)
        add = appsecret + uid + str(ts)
        h1 = hashlib.md5()
        h1.update(add.encode('utf-8'))
        verify = h1.hexdigest()

        data={
            "appkey":"zhihuishenghuo-gpt3-handler",
            "geo[lat]":39.9041999,
            "geo[lng]": 116.4073963,
            "lang":"",
            "msg": msg,
            "nickname": "tester",
            "timestamp": str(ts),
            "uid": uid,
            "verify": verify,
            "new_session": new_session,
            "extra_info": {
                "top_p": 1,
                "max_tokens": 512,
                "system_prompt": "你来根据我描述的场景和角色说的话，预测对方会有哪些回复的话，最少预测10种不同的回复。"
            }
        }
        #requests.adapters.DEFAULT_RETRIES = 5
        try:
            response = requests.post("http://robot-service-test.centaurstech.com/api/chat",timeout=20,headers=self.header,data=data)
            # result=eval(response.text.encode('utf-8').decode("unicode_escape").replace("\n","").replace(" ",""))
            result = response.text.encode('utf-8').decode("unicode_escape").replace("\n", "").replace(r'"', "")
            res = re.search(r"msg:(.*?),", result)
            if res:
                result = res[0].replace("msg: ", "").replace(",", "")
            # print(result)
            # return result
            result_text = result.replace("。", "")
            result_split = result_text.split(".")
            result_split_text = []
            for i in result_split:
                if not i.isdigit():
                    new_string = re.sub(r'\d+', '', i)
                    result_split_text.append(new_string)
            print(result_split_text)
            return result_split_text
        except Exception as err:
            print('An exception happened: ' + str(err))



    def text_output(self,text2):
        text_list=[]
        # text=self.get_gptresponse(msg="你是该场景的主人公请就{}这个场景给我十个你在这时会说的话".format(self.get_textresponse()))
        # text_list.extend(text)
        for i in range(5):
            text_append=self.get_gptresponse(msg="你是该场景的主人公请就{}这个场景给我十个你在这时会说的否定意图的话".format(text2),new_session=False)
            text_list.extend(text_append)
        for i in range(6):
            text_append=self.get_gptresponse(msg="你是该场景的主人公请就{}这个场景给我十个你在这时会说的肯定意图的话".format(self.get_textresponse()),new_session=False)
            text_list.extend(text_append)
        print(text_list)
        return text_list
        # for i in text_list:
        #     self.get_textresponse(title=i)

    def repeat(self,f,title="打开天选之子"):
        result=""
        request_list=[]
        util=Util()
        text2,text3,text4,zipped=util.open_text()
        return_value = f(title=title)
        print(return_value)
        if return_value.__eq__(text2[0]):
            result = "T"
        else:
            result="F"
        print(result)
        for i in text2:
            type_list= re.search(r"{(.*?)}", i)
            if type_list:
                number=type_list[0]
                number_1=type_list[0].replace("{", "").replace("}", "")
        for i in zipped:
            type_list1 = re.search(r"\[(.*?)]", i[1])   #[]
            type_list2 = re.search(r"{(.*?)}", i[0])    #{}
            type_list3 = re.search(r"\((.*?)\)", i[0])  #()
            if type_list2:
                number2 = type_list2[0]
                number2_1 = type_list2[0].replace("{", "").replace("}", "")
            if type_list3:
                number3 = type_list2[0]
            else:
                number3 = None
            if type_list1:
                number1=type_list1[0]
                number1_1=type_list1[0].replace("[","").replace("]","")
                for j in i[1].replace(number1,"").split("|"):
                    print(j)
                    time.sleep(3)
                    return_value = f(title=j, new_session=False)
                    print(return_value)





    def run_test(self):
        self.repeat(self.get_textresponse, title="打开天选之子")







if __name__ == '__main__':
    #GPT().get_gptresponse()
    #GPT().get_textresponse(title="打开天选之子",new_session=False)
    #GPT().text_output()
    GPT().run_test()
