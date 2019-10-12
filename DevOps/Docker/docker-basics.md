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
- Run the interactive shell from docker image: `docker run -i -t <image-name>`
	Eg: `docker run -i -t centos`
- Get IP of a container: `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container-id>`
	Eg: `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 40ea8efbb688`
- Get log path of a container: `docker inspect --format='{{.LogPath}}' <container-name>`	
	Eg: `docker inspect --format='{{.LogPath}}' my-container`
- Copy file to local system from docker container: `docker cp <container-name>:<source-file-path-in-container> <dest-file-path-local>`
	Eg: `docker cp kerberos:/tmp/reader.user.keytab .`
- Login to docker container: `docker exec -it <container-id> bash`
	Eg: `docker exec -it 3dfbc8ef00f5 bash`
- Run shell commands in container without login : `docker exec -i <container-name> sh -c '<shell-command>'`
	Eg: `docker exec -i kafka-single-node_kafka_1 sh -c 'ls -l'`
- Create a network for docker container: `docker network create -d bridge --subnet <subnet> <network-name>`
	Eg: `docker network create -d bridge --subnet 172.25.0.0/16 my-network`
- Add containers to the create network: `docker network connect <network-name> <container-id>`
	Eg: `docker network connect my-network 489936f4e16a`