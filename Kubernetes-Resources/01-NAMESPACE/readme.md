to create a resource run the below command
kubectl create -f namespace.yaml

[ec2-user@ip-172-31-86-12 ~]$ kubectl create -f namespace.yaml 
namespace/roboshop created

kubectl get namespaces

to delete the resources
kubectl delete -f namespace.yaml

[ec2-user@ip-172-31-86-12 ~]$ kubectl delete -f namespace.yaml 
namespace "roboshop" deleted

[ec2-user@ip-172-31-86-12 ~]$ kubectl apply -f  namespace.yaml 
namespace/roboshop created

What apply do here if the resource is there it'll skipp, if not then it'll create it.
