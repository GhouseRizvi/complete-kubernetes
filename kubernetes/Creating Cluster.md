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
  region: us-east-1a

managedNodeGroup:

# instance type default to [m5.large]
- name: spot-1
  spot: true
  ssh:
    publicKeyName: givethename



