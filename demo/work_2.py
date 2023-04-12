'''
dict_ = {"name":"清安","age":18}
如何删除指定键"age"，以及合并字典dict_1 = {"sex":"男"}
'''
dict_ = {"name":"清安","age":18}
dict_1 = {"sex":"男"}
print(dict_.keys())
print(dict_.items())
del dict_["age"]
dict_1.pop("name")
dict_.update(dict_1)
dict_["sex"]="男"
print(dict_)
