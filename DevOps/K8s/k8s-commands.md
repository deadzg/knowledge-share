
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