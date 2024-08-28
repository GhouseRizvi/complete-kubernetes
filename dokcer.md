Container is a Running version of image
image is a static single file.
ex ubuntu is a image it can run on any machine as OS
Docker image is a static file --> it can run any number of containers
image = baseOS (also known as bare minimum os)
container = OS + application + configuration
ex: nginx=debian os + nginx service installed

## if you want container to keeep alive it should run acommand for infinite time

docker image are having bare minimum os withoug extra configurations
Based on the requirement choose the OS
if nginx is webserver almalinux/alpine is enough
or you can take the official image.

Crearting you images

###### How to push images to registry
docker login 192.168.56.12:5000

docker push [docker-jhub-url]/[username]/[imagename]:version

tagging the image
docker tag from:v1 e55b-122-167-172-99.ngrok-free.app/docker-reg/from:v1

pushing the image
docker push e55b-122-167-172-99.ngrok-free.app/docker-reg/from:v1

# How to delete all the running container at a time
docker ps -a -q  it'll give container ids
nowe
docker rm -f `docker ps -a -q`

