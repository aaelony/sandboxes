FROM python:3.7.5-slim

# Set up and activate virtual environment
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

## Dependencies needed for tensorflow (?)
## RUN apt-get update && \
##	apt-get install	python3-libnvinfer-dev uff-converter-tf 


# Python commands run inside the virtual environment
RUN python -m pip install \
        parse \
        realpython-reader
RUN python -m pip install --upgrade pip
RUN python -m pip install numpy>=1.18.1 scipy scikit-learn seaborn pandas matplotlib \
	tensorflow>=2.1 keras torch torchvision h2o





