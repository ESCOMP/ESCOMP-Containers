ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/centos8

ARG ESMF_BRANCH=""

# Build ESMF ==================================================================

RUN mkdir -p /tmp/sources && \
    cd /tmp/sources && \
    git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git && \
    cd esmf && \
    export ESMF_DIR=/tmp/sources/esmf && \
    export ESMF_COMM=mpich3 && \
    export ESMF_BOPT="g" && \
    export ESMF_NETCDF="nc-config" && \
    export ESMF_INSTALL_PREFIX=/usr/local && \
    export ESMF_INSTALL_BINDIR=${ESMF_INSTALL_PREFIX}/bin && \
    export ESMF_INSTALL_DOCDIR=${ESMF_INSTALL_PREFIX}/doc && \
    export ESMF_INSTALL_HEADERDIR=${ESMF_INSTALL_PREFIX}/include && \
    export ESMF_INSTALL_LIBDIR=${ESMF_INSTALL_PREFIX}/lib && \
    export ESMF_INSTALL_MODDIR=${ESMF_INSTALL_PREFIX}/mod && \
    export ESMF_TESTEXHAUSTIVE="OFF" && \
    make info && \
    make -j $(nproc) && \
#    make check && \
    make install

# Build ESMPy =================================================================

RUN export ESMF_DIR=/tmp/sources/esmf && \
    export ESMFMKFILE=/usr/local/lib/esmf.mk && \
    cd ${ESMF_DIR}/src/addon/ESMPy && \
    pip3 install numpy nose && \
    python setup.py build --ESMFMKFILE=${ESMFMKFILE} && \
#    python setup.py test && \
    python setup.py install && \
    cd && \
    python -c "import ESMF"

# Do not remove sources for development builds. These are used for testing.
ENV ESMF_DIR=/tmp/sources/esmf
ENV ESMPY_DIR=${ESMF_DIR}/src/addon/ESMPy
