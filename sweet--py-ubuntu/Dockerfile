FROM ubuntu:18.04

RUN apt-get update -y && \
	apt-get install --assume-yes software-properties-common build-essential \
	cmake gcc && \
	add-apt-repository ppa:deadsnakes/ppa && \
	apt-get install --assume-yes python3.7 python3-venv

# Set up and activate virtual environment
ENV VIRTUAL_ENV "/venv"
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Python commands run inside the virtual environment
RUN python3 -m pip install --upgrade pip && \
	python3 -m pip install setuptools>=41.0.0 Theano
RUN python3 -m pip install parse realpython-reader \
	numpy>=1.18.1 scipy scikit-learn seaborn pandas matplotlib bokeh \
	statsmodels tensorflow>=2.1 keras torch torchvision h2o pytest pymc3






