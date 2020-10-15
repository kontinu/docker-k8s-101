# docker-k8s-101


# docker build
> como compilo o genero una nueva imagen?

`docker build -t kontinu/docker-k8s-101:v1.0 .`

# correr container

`docker container run -it -p 9090:5000 kontinu/docker-k8s-101:v1.0`