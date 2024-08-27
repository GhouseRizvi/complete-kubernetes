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