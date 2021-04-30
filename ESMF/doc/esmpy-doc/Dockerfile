FROM ubuntu

ENV _DEBIAN_FRONTEND=$DEBIAN_FRONTEND
# Avoid having to interact with terminal when installing time-related packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get --yes update && apt-get --yes install latexmk texlive-fonts-recommended \
    texlive-latex-recommended texlive-latex-extra build-essential gfortran git \
    python3-pip
ENV DEBIAN_FRONTEND=$_DEBIAN_FRONTEND
ENV _DEBIAN_FRONTEND=""

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

ENV ARTIFACTS=/artifacts/doc-esmpy
RUN mkdir -p ${ARTIFACTS}

WORKDIR /opt/
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git

ENV ESMF_DIR=/opt/esmf
ENV ESMF_INSTALL_PREFIX=/usr/local
ENV ESMF_INSTALL_BINDIR=${ESMF_INSTALL_PREFIX}/bin
ENV ESMF_INSTALL_DOCDIR=${ESMF_INSTALL_PREFIX}/doc
ENV ESMF_INSTALL_HEADERDIR=${ESMF_INSTALL_PREFIX}/include
ENV ESMF_INSTALL_LIBDIR=${ESMF_INSTALL_PREFIX}/lib
ENV ESMF_INSTALL_MODDIR=${ESMF_INSTALL_PREFIX}/mod

WORKDIR ${ESMF_DIR}
RUN make 2>&1 | tee esmf-make.out
RUN make install 2>&1 | tee esmf-make-install.out

ENV ESMFMKFILE=${ESMF_INSTALL_LIBDIR}/esmf.mk
RUN pip3 install sphinx sphinxcontrib-packages sphinxcontrib-bibtex==1.0.0 numpy nose

WORKDIR ${ESMF_DIR}/src/addon/ESMPy
RUN python3 setup.py build
WORKDIR doc
RUN make html latexpdf 2>&1 | tee ${ARTIFACTS}/esmpy-make-doc.out

RUN cp -r esmpy_doc ${ARTIFACTS} && \
    cd /artifacts && \
    zip -r doc-esmpy.zip doc-esmpy
