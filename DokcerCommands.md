for filtering
docker images --filter "label=Author=Ghouse"
docker inspect 31f9928b98a2(image id) 

to know the env variable
docker run env:v1 env
 docker ps -a --no-trunc
 docker system prune 
 
 

Unix

To delete all containers including its volumes use,

docker rm -vf $(docker ps -aq)

To delete all the images,

docker rmi -f $(docker images -aq)
