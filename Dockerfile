From continuumio/miniconda3

ADD ./environment.yml .
RUN conda env create
RUN echo "conda activate chem-bot" >> ~/.bashrc

ADD . ./root
WORKDIR /root
# workaround: 
# https://stackoverflow.com/questions/46652928/shell-into-a-docker-container-running-on-a-heroku-dyno-how
RUN ln -s /bin/bash /bin/sh
