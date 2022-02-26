From rocker/rstudio:4.1.1

RUN apt-get update && apt-get install -y build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev libxml2-dev libglpk-dev libnode-dev libv8-dev

RUN install2.r --error remotes

RUN install2.r --error data.table curl h2o bayesplot tidyverse pander logger comorbidity neatRanges plumber igraph

RUN install2.r --error rstan
RUN R -e 'remotes::install_github("stan-dev/cmdstanr", upgrade = "always")'
RUN R -e 'remotes::install_github("paul-buerkner/brms", upgrade = "always")'

RUN install2.r --error shinystan
