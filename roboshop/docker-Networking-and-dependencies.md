web
mongodb
catalogue
connect web to catalogue
user module

1. Web is runnning
2. Mongodb is running
3. Catalogue is running
Now how to connect catalogue to web

curretly catalogue is not connected to mongdb getting the below error when seeing the docker logs
{"level":"error","time":1725086912210,"pid":1,"hostname":"8a979f62a8a6","msg":"ERROR {\"name\":\"MongoNetworkError\"}","v":1}

Here containers should have proper names to connect with each other
docker run -d --name mongodb mongodb:v1

By defalut hostname is not be configured to connect, if you ping with ip address it'll connect

Docker Networking:
Here we have 
1. Bridge Network
2. Host Network
3. None Network
4. overlay network

docker network ls (it'll give all the docker networks)

default bridge network cannot ressolve on hostnames
docker recommends to create our own bridge networks
ip a
docker0 is network created by docker
when created catalogue it'll get the ip adrres from here 172.17.0.2
similarly mogodb gets 172.17.0.3
in the docker default network
so here for roboshop i'm creating a network
# docker network create roboshop
Creating network is helpful isolating your projects according to name of each project and you can isolate them in thier own network
-> Container are isolated from other projects
-> You can create multiple networks for different projects
-> You can connect multiple containers to same network
-> You can connect multiple networks to same container
-> hostname communication can be established

connecting containers to a network
#  docker network connect roboshop mongodb
# docker inspect mongodb | grep -i networkid
# docker network connect roboshop catalogue
# docker run -d --name catalogue --network roboshop catalogue:v1



