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
RUN pwd
RUN ls

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

RUN pwd
RUN ls

RUN git clone https://github.com/esmf-org/esmf-test-scripts.git scripts-git

RUN pwd
RUN ls

RUN cp scripts-git/API_change_script/harvestAPIsFromRefDoc.py .
RUN chmod +x harvestAPIsFromRefDoc.py

RUN cp scripts-git/API_change_script/_harvestAPIs .
RUN chmod +x _harvestAPIs

RUN pwd
RUN ls

RUN ./_harvestAPIs

RUN pwd
RUN ls

RUN cp -rv APIs*.out ${ESMF_ARTIFACTS}/
RUN cp -rv diff*.out ${ESMF_ARTIFACTS}/

RUN zip -r ${ESMF_ARTIFACTS}/api_change-artifacts.zip ${ESMF_ARTIFACTS}
