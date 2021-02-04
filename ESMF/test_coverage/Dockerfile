ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/esmf-doc-base

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

ENV ESMF_ARTIFACTS=/log
RUN mkdir -p ${ESMF_ARTIFACTS}

WORKDIR ${HOME}/sandbox/esmf
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git src-git

ENV ESMF_DIR=${HOME}/sandbox/esmf/src-git

RUN mkdir log

ENV LOGDIR=${HOME}/sandbox/esmf/log

RUN export ESMF_DIR=${HOME}/sandbox/esmf/src-git
RUN export LOGDIR=${HOME}/sandbox/esmf/log

RUN git clone https://github.com/esmf-org/esmf-test-scripts.git
RUN cp -rv esmf-test-scripts/test_coverage_script/test_coverage  test_coverage.sh
RUN chmod +x test_coverage.sh

WORKDIR ${ESMF_DIR}
RUN bash ${HOME}/sandbox/esmf/test_coverage.sh

WORKDIR ${HOME}/sandbox/esmf
RUN cp -rv log ${ESMF_ARTIFACTS}

RUN zip -r ${ESMF_ARTIFACTS}/test_coverage-artifacts.zip ${ESMF_ARTIFACTS}
