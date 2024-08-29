FROM almalinux
#CMD [ "ping" ,"-c5","google.com"]
# when container runs it'll ping goole 5 times by default
#we can overide this 
#docker run entry:v1 ping -c 5 facebook.com
#that conclude CMD can be overridden
#ENTRYPOINT [ "ping" ,"-c5","google.com"]
#so here we cannot override the entruypoint
#for best result we do cmd and entrypoint in combination 
CMD [ "google.com" ]
ENTRYPOINT [ "ping","-c5" ]
