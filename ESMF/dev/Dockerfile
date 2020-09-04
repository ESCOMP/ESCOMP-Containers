ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/centos8

ARG ESMF_BRANCH=""

# Build ESMF ==================================================================

ENV ESMF_DIR=/tmp/sources/esmf
ENV ESMPY_DIR=${ESMF_DIR}/src/addon/ESMPy
ENV ESMFMKFILE=/usr/local/lib/esmf.mk

ENV ESMF_COMM=mpich3
ENV ESMF_BOPT="g"
ENV ESMF_NETCDF="nc-config"
ENV ESMF_INSTALL_PREFIX=/usr/local
ENV ESMF_INSTALL_BINDIR=${ESMF_INSTALL_PREFIX}/bin
ENV ESMF_INSTALL_DOCDIR=${ESMF_INSTALL_PREFIX}/doc
ENV ESMF_INSTALL_HEADERDIR=${ESMF_INSTALL_PREFIX}/include
ENV ESMF_INSTALL_LIBDIR=${ESMF_INSTALL_PREFIX}/lib
ENV ESMF_INSTALL_MODDIR=${ESMF_INSTALL_PREFIX}/mod
ENV ESMF_TESTEXHAUSTIVE="ON"

RUN mkdir -p /tmp/sources && \
    mkdir -p /tmp/artifacts && \
    cd /tmp/sources && \
    git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git && \
    cd esmf && \
    make info 2>&1 | tee /tmp/artifacts/esmf-make-info.out && \
    make -j $(nproc) 2>&1 | tee /tmp/artifacts/esmf-make.out && \
#    make check && \
    make install 2>&1 | tee /tmp/artifacts/esmf-make-install.out

# Build ESMPy =================================================================

RUN cd ${ESMPY_DIR} && \
    pip3 install numpy nose && \
    python setup.py build --ESMFMKFILE=${ESMFMKFILE} && \
#    python setup.py test && \
    python setup.py install && \
    cd && \
    python -c "import ESMF"

RUN cd /tmp && zip -rv artifacts.zip artifacts

WORKDIR ${ESMF_DIR}
