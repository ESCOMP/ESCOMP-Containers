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

RUN mkdir log

ARG homedir=`pwd`
RUN echo "homedir=$homedir"

ARG ESMF_DIR=$homedir/esmf
RUN echo "ESMF_DIR=$ESMF_DIR"

ARG LOGDIR=$homedir/log
RUN echo "LOGDIR=$LOGDIR"


#########################################################
# clone ESMF-TEST-SCRIPTS and RUN TEST COVERAGE SCRIPT  #
#########################################################

RUN git clone https://github.com/esmf-org/esmf-test-scripts.git
RUN cp -r esmf-test-scripts/test_coverage_script/* .

RUN cd $ESMF_DIR
RUN $homedir/test_coverage
RUN cd ..

######################################################
# clone ESMF-TEST-ARTIFACTS and TEST COVERAGE PUSH   #
######################################################

RUN git clone https://github.com/esmf-org/esmf-test-artifacts.git

RUN cd esmf-test-artifacts
RUN mkdir test_coverage
RUN cd test_coverage
RUN cp $LOGDIR/ESMF_*  .
RUN cp $LOGDIR/ESMC_*  .
RUN cp $LOGDIR/Methods_Tests  .
RUN cd ..
RUN git add .
RUN git commit -a -m " Test Coverage log pushed in artifacts [ci skip] "
RUN git push origin master
