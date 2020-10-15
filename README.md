# docker-k8s-101

# Docker
## docker build
> como compilo o genero una nueva imagen?

`docker build -t kontinu/docker-k8s-101:v1.0 .`

## correr container

`docker container run -it -p 9090:5000 kontinu/docker-k8s-101:v1.0`

# ===== ORCHESTRATORS =====

# docker-compose [single engine]

`docker-compose up`

# Docker Swarm

> viz
```
docker service create \
  --name=viz \
  --publish=8080:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer
```


---
# ECS

```bash
ecs-cli configure --cluster kontinu-ecs --default-launch-type EC2 --config-name kontinu-ecs --region us-east-2

ecs-cli configure profile --access-key $aws_access_key_id --secret-key $aws_secret_access_key --profile-name kontinu-ecs-profile


ecs-cli up --keypair gitlab-devops-bootcamp --capability-iam --size 1 --instance-type t2.small --cluster-config kontinu-ecs --ecs-profile kontinu-ecs-profile

# up and run application
ecs-cli compose up --create-log-groups --cluster-config kontinu-ecs --ecs-profile kontinu-ecs-profile


ecs-cli compose down --cluster-config kontinu-ecs --ecs-profile kontinu-ecs-profile

ecs-cli compose service up --cluster-config kontinu-ecs --ecs-profile kontinu-ecs-profile


ecs-cli compose service rm --cluster-config kontinu-ecs --ecs-profile kontinu-ecs-profile

ecs-cli down --force --cluster-config kontinu-ecs --ecs-profile kontinu-ecs-profile

```