from datetime import datetime

import yaml


class Util:
    @classmethod
    def get_conf(cls):
        with open('../config/conf_get_excel','r',encoding='UTF8') as f:
            data=yaml.load(f,Loader=yaml.FullLoader)
            return data

    @classmethod
    def get_current_time(self):
        return datetime.now()  #得到当前时间

if __name__ == '__main__':
        print(Util.get_conf())