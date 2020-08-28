ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/esmpy-doc-base

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

ENV ARTIFACTS=/artifacts/doc-esmpy
RUN mkdir -p ${ARTIFACTS}

WORKDIR /opt/
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git esmpy-doc-build

WORKDIR esmpy-doc-build/src/addon/ESMPy
RUN python3 setup.py build
WORKDIR doc
RUN make html latexpdf 2>&1 | tee /artifacts/doc-esmpy/esmpy-make-doc.out

RUN cp -r esmpy_doc ${ARTIFACTS} && \
    cd /artifacts && \
    zip -r doc-esmpy.zip doc-esmpy
