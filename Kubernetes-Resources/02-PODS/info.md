to get the list of pods
kubectl get pods
 to get the pods under namespace
 kubectl get pods -n roboshop

 to login into container
 kubectl exec -it roboshop-mongodb-0 -- /bin/bash

 to login a particular container
 kubectl exec -it multi -c sidecar --bash

 # In pods if we have a multiple container they use the same network
 #  and same port. So we can't have multiple container with same port number.

# to delete the pods
[ec2-user@ip-172-31-23-51 02-PODS]$ kubectl delete -f multi-container.yaml

during the pod creation it'll pull the image and started the app
meanwhile if the image is updated and pushed to the registry, and now image is chenged on the same version

but if you apply pod since image is already running, it'll not pull the latest image.

if the image already existed in the cluster and new changes on the image has been pushed to registry, during apply pod it'll not fetch the latest image from the repository.

## so here in kubernetes we've image pull policy 
# 1. Always: it'll always pull the image from the registry
# 2. Never: it'll never pull the image from the registry