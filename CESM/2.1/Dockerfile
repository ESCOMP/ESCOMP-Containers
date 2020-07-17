##############################
# ESCOMP/CESM/2.1 Dockerfile #
##############################

# Use the ESCOMP centos8 base - this is a base install of CentOS, plus NetCDF/HDF5/PNetCDF/MPICH
FROM escomp/base-centos8

# Install CESM:
COPY Files/ea002e626aee6bc6643e8ab5f998e5e4 /root/.subversion/auth/svn.ssl.server/
RUN mkdir -p /opt/ncar && \
    cd /opt/ncar && \
    git clone -b release-cesm2.1.3 https://github.com/ESCOMP/cesm.git cesm2 && \
    cd cesm2 && \
    ./manage_externals/checkout_externals 

# Set up the environment - create the group and user, the shell variables, the input data directory and sudo access:
RUN groupadd ncar && \
    useradd -c 'CESM User' -d /home/user -g ncar -m -s /bin/bash user && \
    yum install -y ftp && \
    echo 'export CESMDATAROOT=${HOME}' >> /etc/profile.d/cesm.sh && \
    echo 'export CIME_MACHINE=container' >> /etc/profile.d/cesm.sh && \
    echo 'export USER=$(whoami)' >> /etc/profile.d/cesm.sh && \
    echo 'export PS1="[\u@cesm2.1.3 \W]\$ "' >> /etc/profile.d/cesm.sh && \
    echo 'export PATH=${PATH}:/opt/ncar/cesm2/cime/scripts' >> /etc/profile.d/cesm.sh && \
    echo 'user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/ncar 


# Add the container versions of the config_machines & config_compilers settings - later, integrate these into CIME
COPY Files/config_compilers.xml /opt/ncar/cesm2/cime/config/cesm/machines/
COPY Files/config_machines.xml /opt/ncar/cesm2/cime/config/cesm/machines/
COPY Files/config_inputdata.xml /opt/ncar/cesm2/cime/config/cesm/

USER user
WORKDIR /home/user
ENTRYPOINT ["/bin/bash", "-l"]
