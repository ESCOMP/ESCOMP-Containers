##############################
# ESMF/8 Dockerfile          #
##############################

# Use the ESCOMP centos8 base - this is a base install of CentOS, plus NetCDF/HDF5/PNetCDF/MPICH
FROM escomp/base:centos8

ENV ESMF_SLUG="ESMF_8_0_1"

RUN mkdir -p /tmp/sources && \
    cd /tmp/sources && \
    wget -q https://github.com/esmf-org/esmf/archive/${ESMF_SLUG}.tar.gz && \
    tar zxf ${ESMF_SLUG}.tar.gz && \
    cd esmf-${ESMF_SLUG} && \
    export ESMF_DIR=/tmp/sources/esmf-${ESMF_SLUG} && \
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

RUN export ESMF_DIR=/tmp/sources/esmf-${ESMF_SLUG} && \
    export ESMFMKFILE=/usr/local/lib/esmf.mk && \
    cd ${ESMF_DIR}/src/addon/ESMPy && \
    pip3 install numpy nose && \
    python setup.py build --ESMFMKFILE=${ESMFMKFILE} && \
#    python setup.py test && \
    python setup.py install && \
    cd && \
    python -c "import ESMF"

RUN rm -rf /tmp/sources
