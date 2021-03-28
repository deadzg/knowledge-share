# Kind Setup

-Source: https://sookocheff.com/post/kubernetes/local-kubernetes-development-with-kind/

Create local docker registry: `sh local-docker-reg.sh`
Create kind cluster: `kind create cluster --name my-cluster --config=config.yaml`
Connect docker registry to kind cluster - `docker network connect "kind" "kind-registry"`