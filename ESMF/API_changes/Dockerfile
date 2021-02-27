ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/esmf-doc-base

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

ENV ESMF_ARTIFACTS=/artifacts
RUN mkdir -p ${ESMF_ARTIFACTS}

WORKDIR ${HOME}/sandbox/esmf
RUN git clone https://github.com/esmf-org/esmf.git src-git

ENV ESMF_DIR=${HOME}/sandbox/esmf/src-git

RUN export ESMF_DIR=${HOME}/sandbox/esmf/src-git

RUN echo "ESMF_DIR=$ESMF_DIR"

ARG TAG1=""
RUN echo "TAG1=$TAG1"

ENV TAG1=$TAG1
RUN export TAG1=$TAG1

ARG TAG2=""
RUN echo "TAG2=$TAG2"

ENV TAG2=$TAG2
RUN export TAG2=$TAG2

ARG Branch_Tag=""
RUN echo "Branch_Tag=$Branch_Tag"

ENV Branch_Tag=$Branch_Tag
RUN export Branch_Tag=$Branch_Tag

WORKDIR ${HOME}/sandbox/esmf
RUN git clone https://github.com/esmf-org/esmf-test-scripts.git scripts-git

COPY ${HOME}/sandbox/esmf/scripts-git/API_change_script/harvestAPIsFromRefDoc.py ${HOME}/sandbox/esmf/harvestAPIsFromRefDoc.py
RUN chmod +x ${HOME}/sandbox/esmf/harvestAPIsFromRefDoc.py

COPY ${HOME}/sandbox/esmf/scripts-git/API_change_script/_harvestAPIs ${HOME}/sandbox/esmf/_harvestAPIs
RUN chmod +x ${HOME}/sandbox/esmf/_harvestAPIs

RUN ${HOME}/sandbox/esmf/_harvestAPIs

COPY ${HOME}/sandbox/esmf/APIs*.out ${ESMF_ARTIFACTS}/
COPY ${HOME}/sandbox/esmf/diff*.out ${ESMF_ARTIFACTS}/

RUN zip -r ${ESMF_ARTIFACTS}/api_change-artifacts.zip ${ESMF_ARTIFACTS}
