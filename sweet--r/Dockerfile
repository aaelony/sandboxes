FROM rocker/tidyverse

RUN apt-get update && \
	apt-get install -y default-jdk-headless cmake \
	libnode-dev gcc software-properties-common && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN R CMD javareconf

ENV MAKE="make -j4"

RUN install2.r --error ROCR data.table curl coda mvtnorm loo dagitty h2o


ARG CACHE_DATE

RUN install2.r -r http://h2o-release.s3.amazonaws.com/h2o/latest_stable_R h2o

RUN git clone --recursive https://github.com/dmlc/xgboost && \
    cd xgboost && git submodule init && git submodule update && \
    cd R-package && R CMD INSTALL .

RUN R -e 'devtools::install_github("Laurae2/lgbdl"); lgbdl::lgb.dl()'

RUN install2.r rstanarm
## ^^^ completes, but doesn't actually install rstanarm...?

## These commented installs don't work
## RUN Rscript -e 'devtools::install_github("rmcelreath/rethinking")'
##  RUN Rscript -e 'devtools::install_github("paul-buerkner/brms", "stan-dev/rstanarm")'
## RUN R -e 'devtools::install_github("stan-dev/rstanarm", build_vignettes = FALSE)'


CMD ["R","--vanilla"]
