FROM almalinux
ADD https://raw.githubusercontent.com/devopshydclub/vprofile-project/vp-rem/pom.xml /tmp/
ADD crispy_kitchen.zip /tmp/
RUN yum install unzip nginx -y
RUN rm -rf /usr/share/nginx/html/*
#RUN cp -r /tmp/crispy_kitchen/* -d /usr/shar/nginx/html/
CMD [ "nginx","-g","daemon off;" ]
