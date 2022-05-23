##### 搭建外网服务器
'''
1、创建socket对象
2、绑定ip地址
3、开启监听客户端
4、接受客户端信息
5、编写响应头
6、给客户端返回消息

'''


import socket

#1
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2  (10.88.7.67)  参数为元组(ip地址，端口号)
server_socket.bind(('10.88.7.67',9090))
#3
server_socket.listen(128)
#4
client_obj,addr = server_socket.accept()
# print(client_obj)

## 从客户端的 socket 里获取数据
data = client_obj.recv(1024).decode('utf-8')
print(data)
"""
# GET->请求方式    
# /—>请求的路径以及请求参数  
# HTTP/1.1->HTTP的版本号   

#Host: 10.88.7.67:9090 ->请求的服务器地址

Connection: keep-alive
Upgrade-Insecure-Requests: 1

#UA 用户代理，最开始设计的目的，是为了能从请求头里识别浏览器的类型
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3877.400 QQBrowser/10.8.4506.400

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
"""




###编写响应头【每写一个响应头就要换一次行，写完所有的响应头，还需要加个换行】
###向客户端发送响应头
client_obj.send('HTTP/1.1 200 OK\n'.encode('utf-8'))

client_obj.send('content-type:text/html;charset=utf-8\n'.encode('utf-8'))
client_obj.send('\n'.encode('utf-8'))
#6
client_obj.send('<h1 style="color:red">王鹤鸣 爱 张粟素</h1>'.encode('utf-8'))



