#############################################
# Documentation build dependencies for ESMF #
#############################################

FROM ubuntu:18.04

ENV _DEBIAN_FRONTEND=$DEBIAN_FRONTEND
# Avoid having to interact with terminal when installing time-related packages
ENV DEBIAN_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/America/Denver /etc/localtime
RUN apt-get -y update && apt-get -y install texlive-full latex2html perl csh \
    git build-essential zip gfortran
ENV DEBIAN_FRONTEND=$_DEBIAN_FRONTEND
ENV _DEBIAN_FRONTEND=""

########################################
# clone ESMF and run copyright update #
########################################
ARG DOCKER_NAMESPACE=""

ARG ESMF_BRANCH=""
RUN echo "ESMF_BRANCH=$ESMF_BRANCH"

# Clone ESMF
WORKDIR ${HOME}/sandbox/esmf
RUN git clone --branch ${ESMF_BRANCH} --depth 1 https://github.com/esmf-org/esmf.git esmf
RUN cd esmf 
RUN git checkout copyright_update
RUN cd ..


RUN git clone https://github.com/esmf-org/esmf-test-scripts.git
RUN cp -r esmf-test-scripts/copyright_update/replace_string .
RUN chmod +x replace_string

RUN find esmf > outfiles
RUN grep -v "eps" outfiles > no_eps_files
RUN grep -v "vsd" no_eps_files > no_vsd_files
RUN grep -v "cdd" no_vsd_files > no_cdd_files
RUN grep -v "vtk" no_cdd_files >  final_files

RUN ./replace_string -nb -nq -s s/2002\-2020/2002\-2021/g -F final_files

RUN cd esmf
RUN git add .
RUN git commit -a -m " Copyright update pushed at `date` "
RUN git push -u origin copyright_update
