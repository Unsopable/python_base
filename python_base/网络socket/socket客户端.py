"""
1. 创建socket对象
2. 连接服务器
3. 发送内容
4. 关闭客户端
"""

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
###"10.88.73.173"
client_socket.connect(('192.168.43.242',9090))

# client_socket.send('hello'.encode('utf-8'))

"""
############### 下载文本文件 ##############
file_name = input('请输入您需要下载的文件名：')
client_socket.send(file_name.encode('utf-8'))

### 接受服务器的信息
data = client_socket.recv(1024).decode('utf-8')
print(data)
with open('demo.'+file_name.split('.')[1],'w',encoding='utf-8') as f:
    f.write(data)
"""

######### 下载图片文件（图片是二进制储存的，所以不用编码） ################
file_name = input('请输入您需要下载的文件：')
client_socket.send(file_name.encode('utf-8'))


# content = client_socket.recv(102400)
with open('demo.'+file_name.split('.')[1],'wb') as f:
    while True:
        content = client_socket.recv(1024)
        if not content:
            break
        f.write(content)

#关闭套接字
client_socket.close()

