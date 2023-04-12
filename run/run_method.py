import requests


class RunMethod:
    @classmethod
    def get_main(cls,url,data=None,headers=None):
        if data:
            url=url+'?'+data  #如果指定了参数，则将参数加到url后面，用？连接
        if headers:
            return requests.get(url,headers=headers)
        else:
            return requests.get(url)

    @classmethod
    def post_main(cls,url,data,headers=None):
        if headers:
            return requests.post(url, data=data, headers=headers)
        else:
            return requests.post(url, data=data)

