Demo app of a simple flask application that I am trying to deploy in a kubernetes cluster.

I am using my powdermaps.com domain to play around, the kubernetes cluster is from DigitalOcean.

### Flask app
github repo: https://github.com/mrasap/flask

The front end is a simple flask app. It creates a simple sqlite database with a counter. The flask app has two paths:    
- `/` shows the counter
- `/increase` increases the counter

### Docker CLI 101
Guide used: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04   
Documentation: https://docs.docker.com/   
Note: unless you added your username to the docker group, all docker commands should be run with sudo.
   
**Build** a docker image: `docker build [OPTIONS] PATH | URL | -`   
e.g. `docker build .` if you are in the directory of the dockerfile.    
   
**List built** images: `docker images`   
   
**Tag** an image: `docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`   
e.g. `docker tag 0676e230cd2e flask` to tag the image with image_id 0676e230cd2e as 'flask'.

**Run** an image: `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`
e.g. `docker run flask` to run the image that we just tagged as flask (add -it option for interactive shell).
   
**List running** containers: `docker ps [OPTIONS]` (add -a to show all active and inactive containers)   
   
**Inspect** a running container: `docker inspect [OPTIONS] NAME|ID [NAME|ID...]`   
e.g. `docker inspect keen_pike | grep IPAddress` to find the IP address of the container with container name keen_pike
   
**Stop** a container: `docker stop [OPTIONS] CONTAINER [CONTAINER...]`   
e.g. `docker stop keen_pike` to stop our container

**Remove** a container: `docker rm [OPTIONS] CONTAINER [CONTAINER...]`   
e.g. `docker rm keen_pike` to remove our container

**Login** to dockerhub: `docker login [OPTIONS] [SERVER]`   
e.g. `docker login -u mrasap` to login, you will be prompted for your password

**Push** an image to dockerhub: `docker push [OPTIONS] NAME[:TAG]`   
e.g. `docker push mrasap/flask` will push the image to the dockerhub of mrasap


### Kubernetes manifests
github repo: https://github.com/mrasap/flask-kubernetes/


### Helm templating
github repo: https://github.com/mrasap/flask-kubernetes-helm/

### Roadmap of features
[X] Flask demo web app   
[X] Git version control   
[X] Containerized the web app with docker   
[X] Multistage docker container with alpine as base to minimize the size   
[X] non-root user running in the container
[X] Dockerhub repo automatic builds   
[ ] Orchestrate the app with kubernetes   
[ ] Templated the deployment with helm   
[ ] Automated the complete deployment with a bash script   
[ ] Ingress load balancer with nginx-ingress   
[ ] TLS support with cert-manager   
[ ] Upgrade cert-manager to latest build   
[ ] Kubernetes StateFulSet   
[ ] Kubernetes namespaces   
[ ] Kubernetes rbac   
[ ] Postgresql for persistent data   
[ ] Redis for caching   
[ ] ELK stack for logging   
[ ] Prometheus for monitoring?   
[ ] Unittests   
[ ] Jenkins CI pipeline   
[ ] Deployment with Spinnaker   

