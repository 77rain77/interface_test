import xlrd


class Lawyer:
    def openc(self,row=1,col=0):
        wb = xlrd.open_workbook('lawy.xlsx')
        table = wb.sheets()[0]
        print(table)
        wa=table.nrows
        print(wa)
        #ws = wb.active
        # wa = table.rows
        # print(wa)
        # list = []
        # for i in range(wa):
        #     wk = ws.cell(row, col).value
        #     list.append(wk)
        # # return list
        # print(list)
if __name__ == '__main__':
    #pytest.main(['-vs'])
    law=Lawyer()
    #law.req()
    law.openc()