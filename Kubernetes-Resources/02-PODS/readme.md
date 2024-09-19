# in docker smallest deployable unit is container
# in kubernetes the smallest deployable container is pod
# A pod can have multiple containers
# A pod is the basic execution unit in a Kubernetes cluster
# A pod is a logical host for one or more containers
# we can run a complete project in one POD
# in a pod all the container will share same network space and share volume as well.
# a pod can have multiple containers but it can have only one network namespace and one volume mount point.



[ec2-user@ip-172-31-86-12 ~]$ kubectl apply -f pods.yaml 
pod/nginx created

kubectl get pods
ec2-user@ip-172-31-86-12 ~]$ kubectl get pods
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          91s

it is Running now where it is running 
[ec2-user@ip-172-31-86-12 ~]$ kubectl get pods -o wide
NAME    READY   STATUS    RESTARTS   AGE     IP               NODE                            NOMINATED NODE   READINESS GATES
nginx   1/1     Running   0          2m31s   192.168.28.152   ip-192-168-13-86.ec2.internal   <none>           <none>

to get the whole information 
[ec2-user@ip-172-31-86-12 ~]$ kubectl get pods -o yaml

if namespace not provided by default it'll run under defaullt name space

[ec2-user@ip-172-31-86-12 ~]$ vim pods.yaml
[ec2-user@ip-172-31-86-12 ~]$ kubectl apply -f pods.yaml 
pod/nginx created
[ec2-user@ip-172-31-86-12 ~]$ kubectl get pods -n roboshop
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          41s

check the running pods
kubectl get pods -A
kubectl delete -f pods.yaml
kubectl delete pods nginx

to get all the pods under roboshop
kubectl get pods -n roboshop -o wide

[ec2-user@ip-172-31-86-12 ~]$ kubectl get pods -n roboshop -o wide
NAME    READY   STATUS    RESTARTS   AGE   IP               NODE                             NOMINATED NODE   READINESS GATES
nginx   1/1     Running   0          24s   192.168.37.181   ip-192-168-44-112.ec2.internal   <none>           <none>
[ec2-user@ip-172-31-86-12 ~]$ curl 192.168.37.181