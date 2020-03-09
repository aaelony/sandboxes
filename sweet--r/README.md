
The following directory is meant to house a Dockerfile that builds an Rstudio environment
with a get of _useful_ libraries preinstalled.


```
time sudo docker build --build-arg CACHE_DATE=$(date +%Y-%m-%d) -t sweetr .

sudo docker run --rm -it sweetr
```


Brute force cleanup:
```
docker system prune -a
```


