#############################################
# Documentation build dependencies for ESMF #
#############################################

FROM ubuntu:18.04

ENV _DEBIAN_FRONTEND=$DEBIAN_FRONTEND
# Avoid having to interact with terminal when installing time-related packages
ENV DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/America/Denver /etc/localtime
RUN apt-get -y update && apt-get -y install texlive-full latex2html perl csh \
    git build-essential zip gfortran
ENV DEBIAN_FRONTEND=$_DEBIAN_FRONTEND
ENV _DEBIAN_FRONTEND=""

########################################
# clone ESMF  						   #
########################################

ARG DOCKER_NAMESPACE=""

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

# Clone ESMF
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git esmf

ARG ESMF_DIR="esmf/"
RUN echo "ESMF_DIR=$ESMF_DIR"

ARG TAG1="develop"
RUN echo "TAG1=$TAG1"

ARG TAG2="ESMF_8_0_1"
RUN echo "TAG2=$TAG2"

######################################################
# clone ESMF-TEST-SCRIPTS and RUN API_CHANGE_SCRIPT  #
######################################################

RUN git clone https://github.com/esmf-org/esmf-test-scripts.git
RUN cp -r esmf-test-scripts/API_change_script/* .
RUN chmod +x  harvestAPIsFromRefDoc.py

RUN ./_harvestAPIs

######################################################
# clone ESMF-TEST-ARTIFACTS and API LOG PUSH	     #
######################################################

RUN git clone https://github.com/esmf-org/esmf-test-artifacts.git

RUN cd esmf-test-artifacts
RUN mkdir api_change
RUN cd api_change
RUN cp -r ../../APIs*.out .
RUN cp -r ../../diff*.out .
RUN cd ..
RUN git add .
RUN git commit -a -m " API change log pushed in artifacts "
RUN git push origin master
