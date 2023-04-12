import pytest
import requests
import xlrd


class Lawyer:
    def req(self):
        url="https://lawyer-figure-test.heyqiwu.cn/api/lawyerFigure/receiveFormData"
        data={
            "userId":"640ecf3e9a54f80001ace371",
            "msg":"带薪年假条例的立法目的是啥"
        }
        reponse=requests.post(url=url,json=data)
        peopleReply=reponse.json()["payload"]["peopleReply"]
        keywordSet=reponse.json()["payload"]["keywordSet"]
        print(reponse.json())
        print(peopleReply)
        print(keywordSet)

    def openxlsx(self,row=1,col=0):
        wb= xlrd.open_workbook('lawy.xlsx')
        ws = wb.active
        wa=ws.rows
        list=[]
        for i in wa:
            row=row+1
            for j in range(10):
                 col=col+1
                 wk = ws.cell(row, col).value
                 list.append(wk)
        #return list
        print(list)







if __name__ == '__main__':
    #pytest.main(['-vs'])
    law=Lawyer()
    #law.req()
    law.openxlsx()