########################################
# Build and collect ESMF documentation #
########################################
ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/esmf-doc-base

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

# Where documentation artifacts will be stored in the container
ENV ESMF_ARTIFACTS=/artifacts
RUN mkdir -p ${ESMF_ARTIFACTS}

# Clone ESMF
WORKDIR ${HOME}/sandbox/esmf
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git src-git

ENV ESMF_DIR=${HOME}/sandbox/esmf/src-git

# Make the NUOPC documentation
WORKDIR ${ESMF_DIR}/src/addon/NUOPC/doc
RUN make localdoc 2>&1 | tee ${ESMF_ARTIFACTS}/nuopc-make-doc.out

# Make the ESMF documentation
WORKDIR ${ESMF_DIR}
RUN make doc 2>&1 | tee ${ESMF_ARTIFACTS}/esmf-make-doc.out

# Make the ESMF dev guide documentation
WORKDIR ${ESMF_DIR}/src/doc/dev_guide
RUN make 2>&1 | tee ${ESMF_ARTIFACTS}/dev_guide-make-doc.out

# Collect and compress the documentation artifacts
WORKDIR ${ESMF_DIR}
RUN cp -rv doc ${ESMF_ARTIFACTS}/doc-esmf
RUN mkdir ${ESMF_ARTIFACTS}/doc-nuopc
RUN cp -rv src/addon/NUOPC/doc/*.pdf src/addon/NUOPC/doc/NUOPC_refdoc src/addon/NUOPC/doc/NUOPC_howtodoc ${ESMF_ARTIFACTS}/doc-nuopc
RUN mkdir ${ESMF_ARTIFACTS}/doc-dev_guide
RUN cp -rv src/doc/dev_guide ${ESMF_ARTIFACTS}/doc-dev_guide

RUN zip -r ${ESMF_ARTIFACTS}/doc-artifacts.zip ${ESMF_ARTIFACTS}
