ARG DOCKER_NAMESPACE="esmf"
ARG ESMF_BRANCH="develop"

FROM ${DOCKER_NAMESPACE}/esmf:${ESMF_BRANCH}

RUN git clone --depth 1 https://github.com/esmf-org/nuopc-app-prototypes.git
WORKDIR nuopc-app-prototypes
RUN git checkout ${ESMF_BRANCH} || echo "WARNING: ESMF_BRANCH does not exist. Checking out develop" && git checkout develop
RUN ln -s /usr/bin/make /usr/bin/gmake || echo "INFO: gmake symlink already exists"

#tdk:rm
ADD ./Turn_off_some_protos.patch /opt/Turn_off_some_protos.patch
RUN git apply /opt/Turn_off_some_protos.patch

ENV ESMF_ARTIFACTS=/opt/artifacts
RUN mkdir -p ${ESMF_ARTIFACTS}

RUN pip3 install --user unittest-xml-reporting
ADD ./meta_test.py /opt/meta_test.py
ADD ./docker-entrypoint.sh /opt/docker-entrypoint.sh

RUN mkdir -p /outgoing
