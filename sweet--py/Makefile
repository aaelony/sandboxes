
start:

.DEFAULT_GOAL := help


run:
	docker run --rm -it sweet--py

build:
	time sudo docker build --build-arg CACHE_DATE=$(date +%Y-%m-%d) -t sweet--py .

run_ubuntu_tf_py2:
	docker run -it --rm tensorflow/tensorflow bash


# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html


.PHONY: no_targets__ help
no_targets__:
help:
	sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | sort"
