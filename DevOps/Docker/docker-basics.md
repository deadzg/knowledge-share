# Docker 
## Basic Commands

-  Create a dockerfile and add which image to pull from along with other commands
- Build docker image from docker file: `docker build `
- List docker images: `docker images`
- Create a container from docker image: `docker run -p <docker-port>:<host-port> <image-id>`
- Check running containers: `docker ps`
- Stop the docker container: `docker stop <container-id>`
- Tag the image: `docker tag <image-id> <login>/<repo>:tag`
	Eg: `docker tag 2882bb03b808 deadzg/k8s-demo:v2`
- Push docker image to docker hub: `docker push <login>/<repo>`
	Eg: `docker push deadzg/k8s-demo`


