from config.data_config import GlobalVal
from run.run_method import RunMethod
from util.get_data import GetData
from util.op_excel import OperateExcel
from util.util_fun import Util


class RunMain:
    def __init__(self):
        self.data=GetData()
        self.op_excel=OperateExcel()

    def run_test(self):
        row_count=self.data.get_case_lines()
        col_act_result=GlobalVal.get_value('act_result')   #返回实际结果的列
        col_test_result=GlobalVal.get_value('test_result') #返回测试结果的列
        col_exec_time=GlobalVal.get_value('exec_time')   #返回测试的时间
        print(row_count)
        for i in range(1,row_count):
            if self.data.get_is_run(i+1):
                data=self.data.get_request_data(i+1)
                url=self.data.get_url(i+1)
                header=self.data.get_is_header(i+1)
                method=self.data.get_request_method(i+1)
                exp_result=self.data.get_expected_result(i+1)
                result=None
                if method == 'get':
                   result= RunMethod.get_main(url,data,header)  #请求的实际结果
                elif method=='post':
                    result=RunMethod.post_main(url,data,header)
                self.op_excel.write_result(i+1,col_act_result,result.text)

                #判断测试结果
                if ',' in exp_result:
                    exp_result_list=exp_result.split(',')
                    for item in exp_result_list:
                        if item not in result.text:
                            print('测试失败',item,'没在实际结果里面')
                            self.op_excel.write_result(i+1,col_test_result,"测试失败")
                            break
                        else:
                            print('测试通过')
                            self.op_excel.write_result(i+1,col_test_result,"测试通过")
                else:
                    if exp_result in result.text:
                        print('测试通过')
                        self.op_excel.write_result(i+1,col_test_result,"测试通过")
                    else:
                        print("测试失败",exp_result,'没在实际结果里面')
                        self.op_excel.write_result(i + 1, col_test_result, "测试失败")
            else:
                self.op_excel.write_result(i+1,col_act_result,"N/A")
                self.op_excel.write_result(i+1,col_test_result, "N/A")
            self.op_excel.write_result(i+1,col_exec_time,Util.get_current_time())
        self.op_excel.save_file()
if __name__ == '__main__':
    run=RunMain()
    run.run_test()



