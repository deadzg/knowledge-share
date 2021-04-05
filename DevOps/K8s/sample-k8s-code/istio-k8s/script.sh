#!bin/sh

kubectl apply -f istio-ingress.yaml
kubectl apply -f istio-virtualservice.yaml