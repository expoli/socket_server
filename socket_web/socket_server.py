#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
import threading
import socket
import sqlite3
import os

encoding = 'utf-8'
BUFSIZE = 1024


def write_msg_to_db(self,msg):
    
    try:
        string1 = msg[0]
        string2 = msg[1]
        flag1 = msg[2]
        flag2 = msg[3]
        # 连接到SQLite数据库
        # 数据库文件是openwrt.db
        # 如果文件不存在，会自动在当前目录创建:
        conn = sqlite3.connect('/usr/src/myapp/socket_web/db.sqlite3')
        # 创建一个Cursor:
        cursor = conn.cursor()
        # # 执行一条SQL语句，创建openwrt表:
        # try:
        #     cursor.execute('create table socket (id integer primary key autoincrement,\
        #             string1 varchar(1024), string2 varchar(1024),flag1 varchar(128),flag2 varchar(128))')
        # except:
        #     print('数据库已存在，不需要重复建立')
        # 继续执行一条SQL语句，插入一条记录:
        sql = "insert into common_customer (string1,string2,flag1,flag2)"\
            + " values "\
            + "(\""   \
            + string1    \
            + "\""  \
            + ", \""   \
            + string2\
            + "\""  \
            + ", \""   \
            + flag1\
            +"\""\
            + ", \""   \
            + flag2\
            +"\")"

        cursor.execute(sql)
        # 通过rowcount获得插入的行数:
        # 服务端打印日志
        print(cursor.rowcount, "记录插入成功。")
        # 成功消息提示
        success_msg = str(cursor.rowcount) + ' save success!\n'
        # 发送成功消息
        self.client.send(success_msg.encode('ascii'))

        # 关闭Cursor:
        cursor.close()
        # 提交事务:
        conn.commit()
        # 关闭Connection:
        conn.close()

    except:
        # 错误提示
        error_msg = 'data format error, please cheak your data\n'
        # 发送提示
        self.client.send(error_msg.encode('ascii'))
        # 服务端提示
        print('格式错误，请注意数据格式')
 
# a read thread, read data from remote
class Reader(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        
    def run(self):
        # 欢迎消息
        welcome_msg = 'welcome!\n'
        self.client.send(welcome_msg.encode('ascii'))

        while True:
            data = self.client.recv(BUFSIZE)
            if(data):
                # 格式化数据
                try:
                    string = bytes.decode(data, encoding)
                    # 输出收到的信息
                    print(string, end='')
                    # 分割字符串
                    sqilted = string.split()
                    # 打印分割后的
                    print(sqilted)
                    # 储存提示
                    rev_msg = str(sqilted) + '\n'
                    self.client.send(rev_msg.encode('ascii'))
                    # 调用数据库写入
                    write_msg_to_db(self,sqilted)
                # 错误处理
                except:
                    # 收到 ^c 等特殊字符
                    error_msg = 'unsuppsort data, please cheak your data\n'
                    self.client.send(error_msg.encode('ascii'))
                    print('不支持的数据格式')
            else:
                break
        # 断开提示
        print("close:", self.client.getpeername())
 
 
# a listen thread, listen remote connect
# when a remote machine request to connect, it will create a read thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        # 端口号
        self.port = port
        # 创建一个基于IPv4和TCP协议的Socket：
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 开始监听
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)
    def run(self):
        print("listener started")
        while True:
            # cltadd 客户端地址
            client, cltadd = self.sock.accept()
            Reader(client).start()
            cltadd = cltadd
            print("accept a connect")
 

if __name__ == "__main__":
    lst  = Listener(9011)   # create a listen thread
    lst.start() # then start



 
# Now, you can use telnet to test it, the command is "telnet 127.0.0.1 9011"
# You also can use web broswer to test, input the address of "http://127.0.0.1:9011" and press Enter button
# Enjoy it....