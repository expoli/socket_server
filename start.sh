#!/bin/bash

# apt-get update
# sudo apt-get install python3-pip -y
# pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django

python3 /usr/src/myapp/socket_web/socket_server.py &
echo "----------------------------------------"
python3 /usr/src/myapp/socket_web/manage.py runserver 0.0.0.0:8000 --insecure