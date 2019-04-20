FROM python:3

COPY ./sources.list /etc/apt/sources.list 
RUN apt-get update  && \
    apt-get install python3-pip -y --allow-unauthenticated &&\
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple django

EXPOSE 9011
EXPOSE 8000