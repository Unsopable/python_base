####### 用 os.walk直接获取所有文件,在作判断 ######

import os


path_ = os.getcwd()
results = []
for _,_,files in os.walk(path_):
    for file in files:
        #### 分割文件名的前缀和后缀
        (_,hzhui) = os.path.splitext(file)
        ### 判断文件后缀是否是 .py
        if hzhui == '.py':
           results.append(file) 
print(results)