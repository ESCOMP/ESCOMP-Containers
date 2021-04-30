#########################################
# ESCOMP/CESM-Postprocessing Dockerfile #
#########################################

# We're using a CentOS8 base for now:
FROM centos:centos8.3.2011


# Set up some variables for versions of packages & environment needs:
ARG SOURCE_MPI=https://www.mpich.org/static/downloads/3.3.2/mpich-3.3.2.tar.gz
ARG SOURCE_MINICONDA=https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh
ARG SOURCE_POSTPROCESSING="-b cheyenne_update_py3 https://github.com/briandobbins/CESM_postprocessing.git"

# Set up the environment variable for the postprocessing software
ENV POSTPROCESS_PATH=/opt/ncar/cesm_postprocessing


# Set the shell to bash - this helps with some of the conda installation quirks in Dockerfiles
SHELL [ "/bin/bash", "--login", "-c" ]


# We're going to install the dnf plugins, the EPEL repo and the english language pack, then 
# enable the PowerTools repo (for libsz.so, needed by netcdf-devel), upgrade existing
# packages, install a list of prerequisites, and clean up.
# Note: Some packages, like netcdf-devel, are obvious, others like tbb less so, and a few
# like 'which' are just for convenience/debugging
RUN dnf install -y dnf-plugins-core epel-release glibc-langpack-en  &&\
    dnf config-manager --set-enabled powertools                     &&\
    dnf upgrade -y                                                  &&\
    dnf install -y calc                 \
                   diffutils            \
                   gcc                  \
                   gcc-c++              \
                   gcc-gfortran         \
                   git                  \
                   file                 \
                   libnsl               \
                   make                 \
                   ncl-devel            \
                   netcdf-fortran-devel \
                   tbb                  \
                   wget                 \
                   which                &&\
    dnf clean all 


# Now let's download & install MPI, then clean it up:
ENV PACKAGE_MPI=${SOURCE_MPI}
RUN mkdir -p /tmp/mpi                                                &&\
    cd /tmp/mpi                                                      &&\
    curl -sSL ${PACKAGE_MPI} --output mpi.tar.gz                     &&\
    tar zxvf mpi.tar.gz -C . --strip-components=1                    &&\
    ./configure --prefix=/usr/local --disable-fortran --disable-cxx  &&\
    make -j 2 install                                                &&\
    rm -rf /tmp/mpi


# Now let's download, install and init Miniconda, then clean up:
ENV PACKAGE_MINICONDA=${SOURCE_MINICONDA}
RUN mkdir -p /tmp/conda                                   &&\
    cd /tmp/conda                                         &&\
    curl -sSL ${PACKAGE_MINICONDA} --output Miniconda.sh  &&\
    sh Miniconda.sh -b -p /opt/ncar/conda                 &&\
    /opt/ncar/conda/bin/conda init bash                   &&\
    rm -rf /tmp/conda


# Create the cesm-env2 conda environment -- this name is hardcoded in the code, 
# it seems, but may be worth looking into changing later, since everything here 
# could be put in a default python environment, and we'd avoid the complexity of 
# activating non-default conda environments in containers.
# Also note that I've done some effort on installing things by source, which 
# results in a much smaller container, but needs more debugging due to odd issues.
# Finally, using the environment.yml (or specific source versions) makes it easier
# to ensure compatibility at different build times.
COPY Files/environment.yml /
RUN  conda update -n base -c defaults conda                &&\
     conda env create -f /environment.yml                  &&\
     echo "conda activate cesm-env2" >> /root/.bashrc      &&\
     rm /environment.yml                                   &&\
     conda clean --all


# Install CESM Postprocessing tools:
ENV POSTPROCESSING_REPO=${SOURCE_POSTPROCESSING}
RUN mkdir -p /opt/ncar                                     && \
    cd /opt/ncar                                           && \
    git clone ${POSTPROCESSING_REPO} cesm_postprocessing   && \
    cd cesm_postprocessing                                 && \
    ln -s /opt/ncar/conda/envs/cesm-env2 .                 && \
    ./manage_externals/checkout_externals                  &&\
    ./create_python_env -machine container 


# And add the 'activate_this.py' script (used by the CESM Postprocessing scripts)
# Is this deprecrated?  Are we doing something unique?  My Python is pretty bad; ask Jim about this
COPY Files/activate_this.py /opt/ncar/cesm_postprocessing/cesm-env2/bin


CMD ["/bin/bash", "-l"]
