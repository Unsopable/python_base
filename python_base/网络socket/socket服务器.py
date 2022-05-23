"""
建立 socket 服务端
1. 创建socket实例对象
2. 绑定IP地址和端口号
3. 开启接收被人的访问
4. 接受客户端传来的信息
"""

import socket
import os

###创建socket实例对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
###绑定地址 和 端口 "10.88.73.173"
server_socket.bind(('192.168.43.242',9090))
### 开启监听(最多排队128个访问)
server_socket.listen(128)
### 接受客户端传来的信息(返回 客户端信息 和 ip地址)
client_obj,client_addr = server_socket.accept()
###最大接收1024个字节
content = client_obj.recv(1024).decode('utf-8')

'''
############ 传输文本文件  ###################
if os.path.isfile(content):
    # print("这是一个文件")
    #### 打开文件
    with open(content, 'r', encoding='utf-8') as f:
        res = f.read()
        ## 将文件编码，发送给客户端
        client_obj.send(res.encode('utf-8'))
        print(res)
else:
    print("文件不存在")'''

########### 传输图片 ############
if os.path.isfile(content):
    # print('有这文件')
    ##打开图片文件，用二进制读模式
    with open(content,'rb') as f:
        res = f.read()
        ### 将内容发个客户端
        client_obj.send(res)






