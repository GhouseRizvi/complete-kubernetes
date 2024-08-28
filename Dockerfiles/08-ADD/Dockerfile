FROM almalinux
ADD https://raw.githubusercontent.com/devopshydclub/vprofile-project/vp-rem/pom.xml /tmp/
ADD crispy_kitchen.zip /tmp/
RUN yum install unzip httpd -y
RUN service start httpd
RUN rm -rf /var/www/html/*
RUN unzip /tmp/crispy_kitchen.zip -d /var/www/html/
RUN service restart httpd
CMD [ "httpd","-g","daemon off;" ]
