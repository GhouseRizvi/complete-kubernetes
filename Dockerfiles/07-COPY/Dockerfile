FROM almalinux
#RUN yum install epel-release -y
RUN yum install nginx -y
RUN rm -rf /usr/share/nginx/html/*
COPY qi /usr/share/nginx/html/
CMD ["nginx","-g","daemon off;"]
