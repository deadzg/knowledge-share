#!bin/bash

echo "Deleting Namespace..."
kubectl delete ns postgres
echo "Delete Completed"