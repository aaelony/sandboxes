
# sweetr

The following directory is meant to house a [Dockerfile](https://docs.docker.com/engine/reference/builder/) that builds an R environment
with a get of _useful_ libraries preinstalled.


## Build the immutable Docker Image

```
time sudo docker build --build-arg CACHE_DATE=$(date +%Y-%m-%d) -t sweetr .

```

## Run a container based on the image

```
sudo docker run --rm -it sweetr
```


## Brute force cleanup

```
docker system prune -a
```


