# Basics Minikube

## Start minikube
`minikube start`

## Launch the minikube dashboard in browser
`minikube dashboard`

## Fetch service url for service of type nodeport in minikube
`minikube service <service-name> -n <namespace> -url`
Eg:
`minikube service order-service -n order-dev --url`

## Minikube docker image
Since we don't want to pull the images from docker registery, we need to confgiure the minikube docker env and create image in it

Run: `eval $(minikube docker-env)`
Create docker image: `docker build -t <image-name> .`

Set image pull policy to never in deployment yaml file:
`imagePullPolicy: Never`

https://medium.com/bb-tutorials-and-thoughts/how-to-use-own-local-doker-images-with-minikube-2c1ed0b0968