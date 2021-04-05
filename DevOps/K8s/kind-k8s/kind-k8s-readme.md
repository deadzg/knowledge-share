# Kind: Tool to setup K8s cluster locally (Alternative to minikube)
https://kind.sigs.k8s.io/docs/user/quick-start/
Install Kind: `brew install kind`
Create cluster: `kind create cluster --name kind-2`
Create cluster with custom config: `kind create cluster --name my-cluster --config=config.yaml`
https://kind.sigs.k8s.io/docs/user/configuration/
List kind cluster: `kind get clusters`
Delete kid cluster: `kind delete cluster --name kind`

# Kind Setup

-Source: https://sookocheff.com/post/kubernetes/local-kubernetes-development-with-kind/

Create local docker registry: `sh local-docker-reg.sh`
Create kind cluster: `kind create cluster --name my-cluster --config=config.yaml`
Connect docker registry to kind cluster - `docker network connect "kind" "kind-registry"`

## Setup Ingress Control in kind
https://kind.sigs.k8s.io/docs/user/ingress/
