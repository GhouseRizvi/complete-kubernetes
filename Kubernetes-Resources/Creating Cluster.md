EKS Install

Requirement
eksctl
awscli
kubectl

eksctl called ---> aws command line
    first is does it authentication
    after getting the permission it'll go and create the cluster

1. Create IAM user, with admin access
    got aws create IAM user 
        - name eks-admin
        - we don't need aws console access
        - Next
        - attatch policy (admin access)
        - create user
    Once user is created
    - under security credentials
     create access key for command line acces
     save it safe somewhere

how we're going to create Cluster
We can create from ec2 instance we call it Workstation

after spinning the ec2 instance:
# install aws-cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update

# Install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version

# Install kubectl 1.24
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.24.17/2024-07-12/bin/linux/amd64/kubectl
sudo mv kubectl /usr/local/bin/kubectl
chmod +x /usr/local/bin/kubectl
kubectl version

# Authenticate the IAM user:
    aws configure
# created IAM user with admin access, created access key and secret key
# Created EC2
# Upgraded aws-cli
# installed eksctl
# Installed kubectl --> 1.24
# aws configure
# access key and secret key
This is all we've done

every cluster has Master and nodes

# spot-cluster.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: spot-cluster
  region: us-east-1

managedNodeGroups:
  - name: spot-1
    instanceType: t3.medium  # Specify the instance type
    spot: true
    desiredCapacity: 2  # You can define the number of instances if needed
    ssh:
      publicKeyName: docker-key



  # Create cluster
[ec2-user@ip-172-31-86-12 ~]$ eksctl create cluster --config-file=eks-config.yaml

# Authentication file is used here located 
/home/ec2-user/.kub/config (this file is created for authentication)

here is the content of the file

"""
 server: https://19453FC6CDE4DD64D2C57E01379D5785.gr7.us-east-1.eks.amazonaws.com
  name: spot-cluster.us-east-1.eksctl.io
contexts:
- context:
    cluster: spot-cluster.us-east-1.eksctl.io
    user: eks-admin@spot-cluster.us-east-1.eksctl.io
  name: eks-admin@spot-cluster.us-east-1.eksctl.io
current-context: eks-admin@spot-cluster.us-east-1.eksctl.io
kind: Config
preferences: {}
users:
- name: eks-admin@spot-cluster.us-east-1.eksctl.io
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      args:
      - eks
      - get-token
      - --output
      - json
      - --cluster-name
      - spot-cluster
      - --region
      - us-east-1
      command: aws
      env:
      - name: AWS_STS_REGIONAL_ENDPOINTS
        value: regional
      provideClusterInfo: false

"""
What is happening here kubectl using the configuration it'll create nodes in the cluster

# Pods vs Container:
Container is just one
Pod can have multiple containers
[pod is same like container in kubernetes]

##### 
first resource in the kubernetes we create a namespace
ex roboshop
  in the this name space only project roboshop exists (like private vpc)
  logical isolation of project under kubernetes.
###
in kubernetese every resource have apiVersion
  apiVersion:
  kind:
  kind of resource going to use
  ex kind: namespace
  needs to provide the metadata
  metadata:
    name: roboshop
    
# to bring down the cluster




