FROM almalinux
ADD https://raw.githubusercontent.com/devopshydclub/vprofile-project/vp-rem/pom.xml /tmp/
ADD crispy_kitchen.zip /tmp/
RUN yum install unzip nginx -y
RUN unzip /tmp/crispy_kitchen.zip -d /tmp/
RUN rm -rf /usr/share/nginx/html/*
RUN chmod -R 755 /usr/share/nginx/html/
RUN cp -r /tmp/2129_crispy_kitchen/* -d /usr/shar/nginx/html/
CMD [ "nginx","-g","daemon off;" ]
