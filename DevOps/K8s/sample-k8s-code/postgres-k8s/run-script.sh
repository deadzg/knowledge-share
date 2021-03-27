#!bin/bash

echo "Starting the postgres setup in k8s cluster..."
kubectl apply -f postgres-namespace.yaml

echo "Creating namespace...starting"
kubectl apply -f postgres-namespace.yaml
echo "Creating namespace...completed"

echo "Creating statefulset...starting"
kubectl apply -f postgres-statefulset.yaml
echo "Creating statefulset...completed"

echo "Creating service...starting"
kubectl apply -f postgres-service.yaml
echo "Creating service...completed"

