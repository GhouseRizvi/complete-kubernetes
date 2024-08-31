FROM nginx
RUN rm -rf /usr/share/nginx/html/*
RUN rm -rf /etc/nginx/nginx.conf
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/nginx.conf 
ADD static /usr/share/nginx/html/
ENV catalogue_host="catalogue"
ENV catalogue_host="user"