import binascii
import json
import os
import requests
from Crypto import Random
from Crypto.Cipher import DES, AES
from numpy.core import byte

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# 加密函数
def encryption(key, iv, data):
    """
    :param key:加密密钥，8位数据
    :param iv: 偏移量，Only applicable for ``MODE_CBC``, ``MODE_CFB``, ``MODE_OFB``,
            and ``MODE_OPENPGP`` modes，并且长度必须为8
    :param data: 要加密的数据
    :return: 返回密文
    """
    cipher = DES.new(key, DES.MODE_CFB, iv)  # 创建加密对象，以及加密规则
    data = cipher.encrypt(data.encode("utf-8"))  # 对数据进行编码后进行加密
    return binascii.b2a_hex(data)  # 得到加密后的16进制数据
    #生成随机的 24 字节偏移量 iv


    #iv = os.urandom(24)
    # 生成 AES-192 加密算法的密钥 key（长度为 24 字节）
    #key = os.urandom(24)
    # 创建 AES-192 加密算法的 Cipher 对象
    # cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # # 获取 AES-192 加密算法的加密器 encryptor
    # encryptor = cipher.encryptor()
    # # 加密明文数据 plaintext
    # #plaintext = b"Hello, AES-192!"
    # # 对明文数据进行加密，并获取加密后的密文 ciphertext
    # ciphertext = encryptor.update(data) + encryptor.finalize()
    # return ciphertext


# 解密函数
def decryption(key, iv, data):
    """DES解密函数"""
    data = binascii.a2b_hex(data)  # 把十六进制的密文数据转换成二进制数据
    decipher = DES.new(key, DES.MODE_CFB, iv)  # 创建相同的解密规则
    return decipher.decrypt(data).decode()  # 进行解码



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
#data1=str(data)
data=bytes(json.dumps(data))
#print(data)
keys = b"ID+Qa657Vx4GHbjMu3zhDw=="  # 密钥
iv = "DlPDFcnEYI0RSthB5NdAsg=="  # 偏移量
# keys = b"maqudong"  # 密钥
# iv = Random.new().read(8)  # 随机偏移量
ret = encryption(keys, iv, data)
#print(ret)
#r_ret = decryption(keys, iv, ret)
#print(r_ret)
#print(data)
response=requests.post(url=url,headers=headers,data=ret)
response.encoding = 'utf-8'
print(response.text)
#print(response.headers)






