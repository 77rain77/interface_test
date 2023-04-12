import logging

import pytest


class TestApi:

    # 这里传入的参数名要和parametrize中的‘args’相同，传入的列表中的元素会依次传入测试用例中，列表中有几个元素，就生成几个测试用例
    @pytest.mark.parametrize('args',['赵','钱','孙'])
    def test_api1(self,args):
        print(args)

    @pytest.mark.parametrize('args', [['赵',12],['钱',16],['钱',16]])
    def test_api2(self, args):
        print(args)

    @pytest.mark.parametrize('name,age', [['赵', 12], ['钱', 16], ['钱', 16]])
    def test_api3(self, name,age):
        print(name,age)

    data=[{"pse":"123"},{"sf":"145"},{"phh":"1344"}]
    @pytest.mark.parametrize("datas",data)
    def test_blo(self,datas):
        print(datas.values())
        #print(datas['pse'])
        print(datas.get('pse'))








if __name__ == '__main__':
    pytest.main(['-vs'])