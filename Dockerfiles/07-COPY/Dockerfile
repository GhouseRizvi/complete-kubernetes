FROM centos:8
RUN yum install epel-release -y
RUN yum install nginx -y
RUN rm -rf /usr/shar/nginx/html/*
COPY qi /usr/shar/nginx/html/
