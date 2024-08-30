# Volume
by default docker remove everything which runnin the container when its terminated.
upon removing the container and recreate the same container we los the data
so we need to persist the data by mounting the volume in the container.
Docker containers are ephemera, upon removing the container data will be removed

-> so whenever we recreate the container data should not remove for this we need to use Volume
- docker don't have any file system it uses host file system
- using docker volume we can retain the data, and we can map the same volume to the new container.
# where docker store the data 
it is under 
/var/lib/docker/overlay here it'll create a id
/var/lib/docker/overlay/overlay2/1f7a4a1c7c4
# docker volume is a directory on the host machine
All the information stores under random directory
once volume is created
docker will create a directory on the host machine and store the data in that directory
/var/lib/docker/volumes

to create a volume we need to perform
docker volume create <volume-name>
docker volume ls
docker volume inspect <volume-name>
docker run -d -v nginx:/usr/share/nginx/html -p 80:80 nginx

if you create a volume and mount it to the container that is going to remain as long as it goes

you can also map it to the folder
creating folder and attaching to it called as anonymous volumes
it is not docker managed
[ec2-user@ip-172-31-86-245 cafe]$ docker run -d -v /home/ec2-user/cafe:/usr/share/nginx/html -p 80:80 nginx
docker run -d -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root123 mysql


