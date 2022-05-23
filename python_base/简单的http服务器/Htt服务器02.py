''''
1、创建服务器实例
2、绑定地址
3、开始监听（listen）
4、接受客户端（响应头）
'''

import socket


class Make_server():
    def __init__(self,ip,port):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((ip,port))
        self.socket.listen(128)

    def run_forever(self):
        while True:
            client_socket, addr = self.socket.accept()
            data = client_socket.recv(1024)
            ## 提取路径【path】根据不同地址路径，返回不同信息
            path = b'/'
            response_header = 'HTTP/1.1 200 OK\n'
            if data:
                path = data.splitlines()[0].split( )[1]
                # print(path == b'/')
            if path == b'/':
                response_body = '欢迎来到主页面'
            elif path == b'/login':
                response_body = '请登录账号'
            elif path == b'/register':
                response_body = '请注册账号'
            else:
                #页面未找到 404 Page Not Found
                response_header = 'HTTP/1.1 404 Page Not Found\n'
                response_body = '对不起，您要查找的页面不存在'

            response_header += 'content-type:text/html;charset=utf8\n'
            response_header += '\n'
            client_socket.send((response_header + response_body).encode('utf-8'))


my_server = Make_server('0.0.0.0',9090)
my_server.run_forever()

