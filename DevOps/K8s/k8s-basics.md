
# Kubernetes Basics

## Overview
- Kubernetes is a cloud platform that sits at the highest level of abstraction, it's purpose is to provide a place for containerized applications to live and be managed or orchestrated

- A cloud platform

- Open source

- Helps automate DevOps tasks like deployments, scaling and management of containerized apps

- Usually installed on public cloud IaaS provider such as AWS or Azure

- Can be installed in a hybrid cloud env, with nodes of cluster spread out across a private data center eg: Openstack, vSphere and spread across AWS

- Storage orchestration

- Self healing

- Service discover and load-balancing

- Secret and configuration management

- Horizontal auto-scaling

- Automated rollouts and rollbacks

- k8s

  

## Kubernetes Component Architecture

- Cluster : Master and it's Nodes called KNodes

- Kubernetes master component exposes a REST API that we use to interact with the Kubernetes platform

- Master communicates with Kubelet in each node to maintain state of the cluster

- Each KNode can be either a physical or virtual host

- Each Knode contains Kubelet - a component and running process in KNode

- All KNodes must be running a Kubelet process to be considered a KNode

- DevOps interacting with kubectl to create Kubernetes API objects and manage the cluster

- DevOps look at the yaml config files to make sure config is right or create one
KNode : A worker node that participates in a k8s cluster is usually implemented as a virtual or physical host and it runs a Kubelet that communicates with the master node

- kube-apiserver : Is the primary component of the master node, it exposes a REST API that we can post k8s objects (that is, Pod, Deployment) to control the state of the cluster

- kubectl cli tool calls the kube-apiserver to get the desired results

- etcd : It is a highly-available key-value data store used by k8s to store all of the API objects (that is, Pod, Deployment) that we create via the kubectl command-line or by calling the kube-apiserver

- kubelet: It is the primary "node agent" that runs on each node. The kubelet takes a set of PodSpecs that are provided through various mechanisms (primarily through apiserver) and ensures that the containers described in those PodSpecs are running and healthy

- namespaces: Kubernetes supports multiple virtual clusters backed by the same physical cluster. These virtual clusters are called namespaces


### Enterprise distributions:

- RedHat OpenShift

- Canonical

### Fully-managed Kubernetes

- Google GCE

- AWS ECS

- Alibaba cloud

- Azure cloud

 ## Architecture and Design:

### Kubernetes Objects:

- Are the "record of intent" - once created, the k8s system will constantly work to ensure that object exists

- Are persistent entities in the k8s system

- Are used to represent the state of your cluster

- Describes what containerized applications are running, and on which nodes

- Describes the resources available to those applications

- Describes the policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance

- Can be defined as YAML config file with two main parts - spec and status

- The spec which you must provide, describes your desired state for the object - the characteristics that you want the object to have

- The status describes the actual state of the object and is supplied and updated by the k8s system

- Different types of object: Pod object, Service Object, Controller Object, Deployment Object

  

### k8s Pod objects

- A Pod are the smallest and simplest k8s object

- A Pod represents a set of running containers on your cluster

- A Pod typically set up to run single primary container. It can also run optional sidecard containers that add supplementary features like logging

- Pods are commonly managed by a deployment definition/object

### k8s deployment objects

- Deployment objects describe a desired state

- Deployment controller changes the actual state to the desired state at a controlled rate

- We can define deployments to create new ReplicaSets or to remove existing deployments and adopt all their resources with new deployments

### k8s ReplicaSet

- A ReplicaSet ensures that a specified number of pod replicas are running at any given time

- A ReplicaSet provides a mechanism for us to define the number of app instances we would like to maintain

- A ReplicaSet should be defined within a deployment object rather than being manipulated directly

- A ReplicaSet provides declarative updates to pods

### k8s service objects

- A service is an API object that describes how to access applications, such as a set of Pods

- A service is an abstraction which defines a logical set of Pods and a policy by which to access them sometimes called a micro-service

- The kube-proxy in each worker node is responsible for managing virtual IPs for the service

- When we create a service object and specify the type as LoadBalancer, Kubernetes provisions a ClusterIP and NodePort service for us, to which the public balancer will route to

- When using service type LoadBalancer, k8s will provision a load balancer depending on the platform

- In an AWS env, k8s will provision an ELB service



There are four types of services in K8s:
 - ClusterIP
 	- Exposes the service on the cluster internal IP
 	- Default type
 - NodePort
 	- Exposes the service on each Node's IP at static port
 	- A route from NodePort service to ClusterIP is automaticall created
 	- Can connect to service from outside cluster using <NodeIP>:<NodePort>
 - LoadBalancer
 	- Exposes the service externally using cloud providers load balancer
 	- NodePort and CLusterIP service to which external loadbalancer will route are automatically created
 - ExternalName
 	- Maps the service to the contents of the external name field by returning a CNAME record with its value

Headless service: 
  - It doesnot loadbalance req like normal service
  - It just creates a DNS entry to reach each pod using the pod name and the subdomain eg: podname.headless-servicename.namespace.svc.cluster-domain.example
  Eg: my-pod-0.my-pod-headless.kafka.svc.cluster.local
  - It's created like a normal service, but it doesnot have an ip of it's own
  - Just specify ClusterIP: None in the normal service def to make it headless
  - When creating a StatefulSet you need to specify serviceName option in the spec with the headless service name

KNode : A worker node that participates in a k8s cluster is usually implemented as a virtual or physical host and it runs a Kubelet that communicates with the master node

kube-apiserver : Is the primary component of the master node, it exposes a REST API that we can post k8s objects (that is, Pod, Deployment) to control the state of the cluster
kubectl cli tool calls the kube-apiserver to get the desired results

etcd : It is a highly-available key-value data store used by k8s to store all of the API objects (that is, Pod, Deployment) that we create via the kubectl command-line or by calling the kube-apiserver

kubelet: It is the primary "node agent" that runs on each node. The kubelet takes a set of PodSpecs that are provided through various mechanisms (primarily through apiserver) and ensures that the containers described in those PodSpecs are running and healthy	

### Keypoints
 - k8s features a master-slave architecture
 - core component of k8s master is the API server
 - k8s nodes are VM where containers are deployed
 - Each KNode features a Kubelet agent that maintains the state of the node and allows for the communication with the master via heartbeat messages

### Achieving HA:
1. Load-balancing between multiple masters
	- To maintain multiple master nodes, accessed via a load balancer
	- To keep multiple master components up and healthy, but to have only one acting at a time (leveraging lease-lock feature)
	- To have a clustered and replicated etcd storage for redundancy
2. Federation
	- To maintain multiple k8s clusters using a CLI tool, kubefed
	- To provide a federation control plane to manage remote clusters
	- To provide a host cluster to make up the federation control plane
	- To logically group and manage a set of k8s clusters that are geographically distinct across AZ or hetrogeneous (hybrid-cloud)


Note: Federation is preferred way
 - It leverages individual clusters across centers or AZ
 - The load-balancing between HA masters approach only leverages a single k8s cluster, where only master nodes are HA
 - Federation is the better approach for achieving HA when you have more than one cluster


 Scaling k8s:

 Specify replicas while defining the yaml file. It will create the replicaSets accordingly


 Autoscaling in k8s:
 Create HorizontalPodAutoscaler API object by using kubectl or REST API
 In kubectl we use kubectl autoscale command to create an autoscaler for a specified ReplicaSet

 Cluster Autoscaling is supported for:
 - AWS
 - Azure
 - GCE : Google Container Engine
 - GKE : Google Kubernetes Engine

  - Cluster autoscalar runs on k8s master node
  - Cluster autoscalar tool automatically adjusts the size of the k8s
  - Cluster autoscalar is not supported for k8s on all platforms. 
  - It will scale the cluster up if there are pods that failed to run in the cluster due to insufficient resources
  - It will scale down some nodes in the cluster are so underutilized, for an extended period of time, that they can be deleted and their pods will be easily placed on some other, existing nodes
 
 Limitations:
  - No more than 5000 nodes
  - No more that 15000 total pods
  - No more than 300000 total containers
  - No more than 100 pods per node

Service Accounts:
 Service accounts are for processes, which run in pods.

Role Binding:
A role binding grants the permissions defined in a role to a user or set of users. It holds a list of subjects (users, groups, or service accounts), and a reference to the role being granted. 

Cluster Role: system:auth-delegator -> Allows delegated authentication and authorization checks. This is commonly used by add-on API servers for unified authentication and authorization.