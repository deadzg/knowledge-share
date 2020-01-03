# Steps to create Python Docker
- Create image: `docker build -t py4fi:basic .`
- Run the container from the image: `docker run -ti py4fi:basic`
- Detach from the container:  `Ctrl-P+Ctrl-Q`
- Attach to the container again: `docker attach <container-id>`
