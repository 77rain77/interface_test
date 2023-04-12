import json
from util.util_fun import Util


class OperateJson:
    def __init__(self,path=None):
        if path:
            self.path=path
        else:
            self.path=Util.get_conf()['dataJson']
        self.data=self.read_data() #以json对象的形式来保存测试数据

    def read_data(self):
        with open(self.path,encoding="utf8") as f:
            return json.load(f)

    def get_value(self,key):
        return self.data[key]

    #将字典转化为字符串格式，xxx=xxx&xxx=xxx
    def get_value_str(self,dic):
        result=""
        for k,v in dic.items():
            result+=k
            result+="="
            result+=v
            result+="&"
        return result[:-1]#去掉最后一个&

if __name__ == '__main__':
    oj=OperateJson()
    print(oj.get_value_str(oj.get_value('get_search_success')))