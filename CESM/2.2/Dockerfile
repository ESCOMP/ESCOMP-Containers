##############################
# ESCOMP/CESM/2.2 Dockerfile #
##############################

# Use the ESCOMP centos8 base - this is a base install of CentOS, plus NetCDF/HDF5/PNetCDF/MPICH
FROM escomp/base:centos8

# Install CESM:
COPY Files/ea002e626aee6bc6643e8ab5f998e5e4 /root/.subversion/auth/svn.ssl.server/
RUN sudo mkdir -p /opt/ncar && \
    cd /opt/ncar && \
    sudo git clone -b release-cesm2.2.0 https://github.com/ESCOMP/cesm.git cesm2 && \
    cd cesm2 && \
    sudo ./manage_externals/checkout_externals 

# Set up the environment - create the group and user, the shell variables, the input data directory and sudo access:
RUN sudo echo 'export CESMDATAROOT=${HOME}' | sudo tee /etc/profile.d/escomp.sh && \
    sudo echo 'export CIME_MACHINE=container' | sudo tee -a /etc/profile.d/escomp.sh && \
    sudo echo 'export USER=$(whoami)' | sudo tee -a /etc/profile.d/escomp.sh && \
    sudo echo 'export PS1="[\u@cesm2.2 \W]\$ "' | sudo tee -a /etc/profile.d/escomp.sh && \
    sudo echo 'ulimit -s unlimited' | sudo tee -a /etc/profile.d/escomp.sh && \
    sudo echo 'export PATH=${PATH}:/opt/ncar/cesm2/cime/scripts' | sudo tee -a /etc/profile.d/escomp.sh


# Add the container versions of the config_machines & config_compilers settings - later, integrate these into CIME
COPY Files/config_compilers.xml /opt/ncar/cesm2/cime/config/cesm/machines/
COPY Files/config_machines.xml /opt/ncar/cesm2/cime/config/cesm/machines/
COPY Files/config_inputdata.xml /opt/ncar/cesm2/cime/config/cesm/
COPY Files/case_setup.py /opt/ncar/cesm2/cime/scripts/lib/CIME/case/case_setup.py

# Add the container changes to the XML files (to be included in stock CIME soon):
COPY Files/config_compsets.xml /opt/ncar/cesm2/cime_config/
COPY Files/config_pes.xml /opt/ncar/cesm2/cime_config/
COPY Files/configs/cam/config_pes.xml /opt/ncar/cesm2/components/cam/cime_config/
COPY Files/configs/cice/config_pes.xml /opt/ncar/cesm2/components/cice/cime_config/
COPY Files/configs/cism/config_pes.xml /opt/ncar/cesm2/components/cism/cime_config/
COPY Files/configs/pop/config_pes.xml /opt/ncar/cesm2/components/pop/cime_config/
COPY Files/configs/clm/config_pes.xml /opt/ncar/cesm2/components/clm/cime_config/

# Fix for SCAM with GNU in DEBUG mode (ESCOMP/CAM issue #257)
COPY Files/micro_mg3_0.F90 /opt/ncar/cesm2/components/cam/src/physics/pumas/micro_mg3_0.F90

# Fix for issue with mpi-serial:
COPY Files/scam_shell_commands /opt/ncar/cesm2/components/cam/cime_config/usermods_dirs/scam_mandatory/shell_commands

# And add the fixed 'create_scam6_iop' script for SCAM:
COPY Files/create_scam6_iop /opt/ncar/cesm2/components/cam/bld/scripts

ENV CESMROOT=/opt/ncar/cesm2 

CMD ["/bin/bash", "-l"]
