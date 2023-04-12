# from testcases.test_api import TestApi
#
# dict={"kaishi":"jieshu","dafg":"gfdsgsf"}
# for i in dict:
#     print(i)
# res=dict.items()
# for i in res:
#     print(i)
# for keys,value in res:
#     print(f"keys:{keys}   "f"values:{value}")
# for keys in dict.keys():
#     print(keys)
#
# TestApi().test_api1()
import re

a="完美世界第97集在线播放"
mv=re.search(r"[0-9][0-9]",a).group(0)
print(mv)