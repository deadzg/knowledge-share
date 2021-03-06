
# CKAD-K8s-Commands

## Pod

- Save existing pod config in a file
`kubectl get pod <pod-name> -o yaml > <file-name>`
Eg:
`kubectl get pod mypod -o yaml > mypod-def.yaml`

- Delete a pod
`kubectl delete pod <pod-name>`

 - Create a pod from file
`kubectl create -f <file-name>`

- SSH into a pod
`kn exec -it <pod-name> sh`
`kn exec -it <pod-name> bash`
Eg:
`kn exec -it order-deployment-7dd69696ff-tgw7m sh`

- Run a curl command to test internal rest endpoints in pod
`kubectl run <pod-name> --image=radial/busyboxplus:curl -i --tty`
Eg:
`kubectl run curl-smalwe --image=radial/busyboxplus:curl -i --tty`

## Deployment
- Edit a deployment:
`kubectl edit deployment <deployment-name>`

## Configmap
- Get help for configmap create command
`kubectl create configmap --help`

- Create configmap without file
`kubectl create configmap <config-name> --from-literal=<key>=<value>`
Eg:
`kubectl create configmap app-config --from-literal=APP_COLOR=blue`
`kubectl create configmap app-config --from-literal=APP_COLOR=blue --from-literal=APP_USAGE=be`

- Create configmap with file
`kubectl create configmap <config-name> --from-file=<path-to-file>`
Eg:
`kubectl create configmap app-config --from-file=app_config.properties`

- Create configmap with file (Declartive approach)
`kubectl create -f <configmap-file-name>`

 - View configmaps
`kubectl get configmaps`

 - Describe configmaps
 `kubectl describe configmap <config-map-name>`

## Secret
- Get help for secret create command
`kubectl create secret --help`

- Create secret without file:
`kubectl create secret generic <secret-name> --from-literal=<key>=<value>`
Eg:
`kubectl create secret generic app-secret --from-literal=DB_HOST=mysql --from-literal=DB_USER=root --from-literal=DB_PASS=passwd`

- Create secret with file:
`kubectl create secret generic <secret-name> --from-file=<path-to-file>`

- Create secret with file (descriptive):
`kubectl create -f <secret-file>`

- Convert content to base64:
`echo -n '<content>' | base64`
Eg:
`echo -n 'password' | base64`

- List secrets
`kubectl get secrets`

- Describe secret
`kubectl describe secret <secret-name>`

## Namespace
- Create namespace:
From file: `kubectl create -f <namespace-def-yaml-file>`
Without file: `kubectl create namespace <namespace-name>`

- Get pods in a given namespace:
`kubectl get pods -n <namespace-name>`
Eg:
`kubectl get pods -n my-namespace`

- Create pod from file in a given namespace:
`kubectl create -f <pod-def-yaml-file> -n <namespace-name>`
Eg:
`kubectl create -f pod-definition.yml -n my-namespace`

- Switch to given namespace permanently
`kubectl config set-context $(kubectl config current-context) --namespace=<namespace-name>`
Eg:
`kubectl config set-context $(kubectl config current-context) --namespace=my-namespace`

- List pods in all namespaces:
`kubectl get pods --all-namespaces`


Ref: https://medium.com/google-cloud/kubernetes-110-your-first-deployment-bf123c1d3f8
Env : Google Cloud Platform


=====Create namespace=====
kubectl create -f k8s-sample-json/namespace-vault.json

Content of Json file:
{
  "kind": "Namespace",
  "apiVersion": "v1",
  "metadata": {
    "name": "vault-eng",
    "labels": {
      "name": "development"
    }
  }
}	

=========================


=====Create Pod=========
---
apiVersion: v1
kind: Pod 
metadata:
 name: nodehelloworld.example.com
 labels:
  app: helloworld
spec:
 containers:
 - name: k8s-demo
   image: deadzg/k8s-demo
   ports:
   - containerPort: 3000

List pods: kubectl get pods
Describe pod: kubectl describe pod nodehelloworld.example.com
Access the service from outside the pod ie. Portforward: kubectl port-forward nodehelloworld.example.com 8081:3000
Expose the service: kubectl expose pod nodehelloworld.example.com --type=NodePort --name nodehello-service
Describe the service created and watch for exposed port: kubectl describe service nodehello-service
Get the url: minikube service nodehello-service --url
List services running on k8s: kubectl get service
Execute commands inside pod: kubectl exec nodehelloworld.example.com -- ls /app


Debug pod: kubectl attach <pod-name> -i
  kubectl exec -it <pod-name> -- bash
   kubectl logs <pod-name>

Data of a container never persists.
You need to use volumes for persisting data

Containers within a pod can communicate using the local port numbers

The LoadBalancer Service will also create a port that is open on every node, that can be used by the AWS LoadBalancer to connect. That port is owned by the Service, so that the traffic can be routed to the correct pod

How does the AWS LoadBalancer routes traffic to the correct pod? The load balancer uses the NodePort that is exposed on all non-master nodes

 kubectl run -i --tty busybox --image=busybox  --restart=Never -- sh


=====Replication Controller======

---
apiVersion: v1
kind: ReplicationController
metadata:
 name: hello-world-controller
spec:
 replicas: 2
 selector:
  app: helloworld
 template:
  metadata:
   labels:
    app: helloworld
  spec:
   containers:
   - name: k8s-demo
     image: deadzg/k8s-demo
     ports:
     - name: nodejs-port
       containerPort: 3000

Use it for horizontal scaling
Only use when the application is stateless

Create replication controller: kubectl create -f helloworld-repl-ctrl.yml
Get list of replication controller: kubectl get rc
Increase/Decreas the replicas: kubectl scale --replicas=4 rc/hello-world-controller
Increase/Decreas the replicas from file: kubectl scale --replicas=4 -f helloworld-repl-ctrl.yml
Delete replication controller: kubectl delete rc/hello-world-controller



=====Create Service Account=====

kubectl create sa vault -n <namespace>

Verify:
kubectl get sa -n <namespace>

================================


=====Create Role Binding=====

kubectl create -f k8s-sample-json/rolebinding.yaml -n <namespace>

Content of rolebinding.yaml:

apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
    name: role-tokenreview-binding-banking
    namespace: vault-eng
roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: 'system:auth-delegator'
subjects:
    -
        kind: ServiceAccount
        name: vault
        namespace: vault-eng

==============================

====Get Secret Token for Service Account======

https://devopscube.com/kubernetes-api-access-service-account/

kubectl get serviceaccount vault -o yaml -n <namespace>

kubectl get secret <secret-name> -o yaml -n <namespace>

kubectl get endpoints | grep kubernetes

curl -k  https://35.197.230.18/api/v1/namespaces -H "Authorization: Bearer <token>"
=============================================


Run Object:
kubectl apply -f gitea.yaml

Get pods:
kubectl get pods

Get logs for a pod:
kubectl logs -f gitea-pod

Delte Object:
kubectl delete -f gitea.yaml

Ref: https://github.com/helm/helm/blob/master/docs/install.md

Install Helm:
$ curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh
$ chmod 700 get_helm.sh
$ ./get_helm.sh

helm init command to initialize the helm charts/repository on your local machine and
Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.
It will deploy a tiller pod in your Kube cluster as Deployment object.
helm init

Verify tiller is installed:
kubectl get pods -n kube-system

Check heml is able to connect to tiller:
helm version
Client: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5
d39fbb4", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.13.1", GitCommit:"618447cbf203d147601b4b9bd7f8c37a5
d39fbb4", GitTreeState:"clean"}

To connect to local tiller:
export HELM_HOST=localhost:44134
helm version # Should connect to local version

Delete Tiller:
kubectl delete deployment tiller-deploy --namespace kube-system
OR
helm reset


Get latest list of charts:
helm repo update

Search for a chart:
helm search mysql

Install a chart:
helm install stable/mysql


Issue: Error: no available release name found
Solution:
- Delete the tiller : kubectl delete deployment tiller-deploy --namespace kube-system
$ kubectl create serviceaccount --namespace kube-system tiller
$ kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
$ helm init --service-account tiller

Features of this MySQL chart: 
helm inspect stable/mysql

Whenever you install a chart, a new release is created. 
So one chart can be installed multiple times into the same cluster. 
And each can be independently managed and upgraded.

List of all deployed releases:
helm ls

Delete a release:
helm delete <release-name>

Check status of helm release:
helm status <release-name>

Rollback the release
helm status <release-name> <release-version>


Charts:
A chart is a collection of files that describe a related set of Kubernetes resources

Directory name is the name of the chart:

wordpress/
  Chart.yaml          # A YAML file containing information about the chart
  LICENSE             # OPTIONAL: A plain text file containing the license for the chart
  README.md           # OPTIONAL: A human-readable README file
  requirements.yaml   # OPTIONAL: A YAML file listing dependencies for the chart
  values.yaml         # The default configuration values for this chart
  charts/             # A directory containing any charts upon which this chart depends.
  templates/          # A directory of templates that, when combined with values,
                      # will generate valid Kubernetes manifest files.
  templates/NOTES.txt # OPTIONAL: A plain text file containing short usage notes


Ref: https://docs.bitnami.com/kubernetes/how-to/create-your-first-helm-chart/
Ref: https://dzone.com/articles/create-install-upgrade-and-rollback-a-helm-chart-p
https://dzone.com/articles/create-install-upgrade-rollback-a-helm-chart-part

Create your chart:
helm create mychart


Check Helm chart lint:
helm lint myhelmchartplanet

Package helm chart:
helm package myhelmchartplanet

Path where the helm chart gets generated:
ls -l .helm/repository/local/  













