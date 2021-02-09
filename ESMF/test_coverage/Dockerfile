ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/esmf-doc-base

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

ENV ESMF_ARTIFACTS=/log
RUN mkdir -p ${ESMF_ARTIFACTS}

WORKDIR ${HOME}/sandbox/esmf
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git src-git

ENV ESMF_DIR=${HOME}/sandbox/esmf/src-git

RUN mkdir store

ENV LOGDIR=${HOME}/sandbox/esmf/store

RUN export ESMF_DIR=${HOME}/sandbox/esmf/src-git
RUN export LOGDIR=${HOME}/sandbox/esmf/store

RUN echo "ESMF_DIR=$ESMF_DIR"
RUN echo "LOGDIR=$LOGDIR"

RUN git clone https://github.com/esmf-org/esmf-test-scripts.git scripts-git
RUN chmod +x scripts-git/test_coverage_script/test_coverage

WORKDIR ${ESMF_DIR}
RUN bash ../scripts-git/test_coverage_script/test_coverage

WORKDIR ${HOME}/sandbox/esmf
RUN cp -rv store/*  ${ESMF_ARTIFACTS}/

RUN zip -r ${ESMF_ARTIFACTS}/test_coverage-artifacts.zip ${ESMF_ARTIFACTS}
