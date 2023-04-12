from config.data_config import GlobalVal
from util.op_excel import OperateExcel
from util.op_json import OperateJson
from util.util_fun import Util


class GetData:

    def __init__(self):
        self.op_excel=OperateExcel()
        self.op_json=OperateJson()
        self.op_header=OperateJson(Util.get_conf()['headerJson'])

    def get_case_lines(self):
        return self.op_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        col=GlobalVal.get_value("is_run")
        flag=self.op_excel.get_value(row,col)
        if flag=='yes':
            return True
        else:
            return False

    #获取请求类型
    def get_request_method(self,row):
        col=GlobalVal.get_value('request_method')
        return self.op_excel.get_value(row,col)

    #获取是否有header
    def get_is_header(self,row):
        col=GlobalVal.get_value('header')
        key=self.op_excel.get_value(row,col)
        if key != 'N/A':
            return self.op_header.get_value(key)
        else:
            return None

    #获取请求地址
    def get_url(self,row):
        col=GlobalVal.get_value('url')
        return self.op_excel.get_value(row,col)

    #获取请求数据
    def get_request_data(self,row):
        col=GlobalVal.get_value('request_data')
        key=self.op_excel.get_value(row,col)
        if key != 'N/A':
            if self.get_request_method(row)=='post':
                return self.op_json.get_value(key)
            elif self.get_request_method(row)=='get':
                return self.op_json.get_value_str(self.op_json.get_value(key))
            else:
                return None

     #获取预期结果
    def get_expected_result(self,row):
        col=GlobalVal.get_value('exp_result')
        return self.op_excel.get_value(row,col)



