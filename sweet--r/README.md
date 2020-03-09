
# sweetr

The following directory is meant to house a [Dockerfile](https://docs.docker.com/engine/reference/builder/) that builds an R environment
with a get of _useful_ libraries preinstalled.


## Build the immutable Docker Image

```
time sudo docker build --build-arg CACHE_DATE=$(date +%Y-%m-%d) -t sweetr .

```

or type `sudo make build_image` instead.


## Run a container based on the image

```
sudo docker run --rm -it sweetr
```

or simply type `make run` instead.


## Brute force cleanup

```
docker system prune -a
```


