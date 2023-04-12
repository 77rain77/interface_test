import json
import quote

from urllib.parse import quote
import requests
from Crypto.Cipher import AES
import base64

def add_to_24(par):
    par = par.encode() #先将字符串类型数据转换成字节型数据
    while len(par) % 16 != 0: #对字节型数据进行长度判断
        par += b'\x00' #如果字节型数据长度不是16倍整数就进行 补充
    return par

headers={
    "Content-Type":"application/json",
    "App-Channel-Id":"xiaowugushiios-phone-sdk-test",
    "app-version":"1.0.0",
    "Authorization":"Bearer 2a8fcd4d-754e-4fae-a32d-59caf9ae2a5d",
    "User-Agent":"XiaoWuStoryPhoneChild\/1.0.0 (iPhone; iOS 16.0; Scale\/2.00)"
}
#url="https://sdk-test.centaurstech.com/api/jiaoyou/v1/works/search"
url="https://account-center-test.chewrobot.com/api/jiaoyou/v1/works/search"
data={
    "searchText":"",
    "type": 1,
    "labels":[
        "标签1",
        "标签2"
    ],
    "page": 1,
    "pageSize": 10
}
data=json.dumps(data)
key = "ID+Qa657Vx4GHbjMu3zhDw=="  # 密钥
#iv = "DlPDFcnEYI0RSthB5NdAsg=="  # 偏移量
iv="DlPDFcnEYI0RSthB"
model = AES.MODE_CBC
aes = AES.new(add_to_24(key),model,add_to_24(iv))
#en_text=aes.decrypt(add_to_24(data))
en_text = aes.encrypt(add_to_24(data)) #加密明文
print(en_text)
#en_text=quote(en_text, 'utf-8')
en_text = base64.encodebytes(en_text) #将返回的字节型数据转进行base64编码
print(en_text)
en_text = en_text.decode('utf8') #将字节型数据转换成python中的字符串类型
print(en_text)
response=requests.post(url=url,headers=headers,json=en_text)
response.encoding = 'utf-8'
print(response.text)

















#int char byte bool float double short long

# password = '123456' #秘钥
# text = '1' #需要加密的内容
# #model = AES.MODE_ECB #定义模式
# model = AES.MODE_CCM
# aes = AES.new(add_to_16(password),model) #创建一个aes对象
#
# en_text = aes.encrypt(add_to_16(text)) #加密明文
# print(en_text)
# en_text = base64.encodebytes(en_text) #将返回的字节型数据转进行base64编码
# print(en_text)
# en_text = en_text.decode('utf8') #将字节型数据转换成python中的字符串类型
# print(en_text.strip())
