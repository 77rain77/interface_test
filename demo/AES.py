# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
#
# # 生成24字节的随机密钥
# key = get_random_bytes(24)
#
# # 生成24字节的随机偏移量
# iv = get_random_bytes(24)
#
# # 创建AES-CBC加密器
# cipher = AES.new(key, AES.MODE_CBC, iv=iv)
#
# # 要加密的明文
# plaintext = b'This is the message to be encrypted'
#
# # 将明文填充到块长度的倍数
# padding_length = AES.block_size - len(plaintext) %AES.block_size
# plaintext += bytes([padding_length]) * padding_length
#
# # 对明文进行加密
# ciphertext = cipher.encrypt(plaintext)
#
# print("Key:", key.hex())
# print("IV:", iv.hex())
# print("Ciphertext:", ciphertext.hex())

a=[1,2,3,5]
b=a
c=a.copy()
print(id(a))
print(id(b))
print(id(c))