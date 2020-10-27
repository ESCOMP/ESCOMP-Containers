################################################################################################################
# escomp/sphinx Dockerfile                                                                                     #
#--------------------------------------------------------------------------------------------------------------#
# A base CentOS8 install + Sphinx & related documentation tools                                                #
################################################################################################################

# Use latest CentOS8:
FROM centos:8

# First, we upate the default packages and install some other necessary ones - while this may give
# some people updated versions of packages vs. others, these differences should not be numerically
# important or affect run-time behavior (eg, a newer Bash version, or perl-XML-LibXML version).

RUN yum -y update && \
    yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
    yum -y install vim emacs-nox git subversion which sudo csh make m4 cmake wget file  && \
    yum -y install python3 git-lfs latexmk texlive-amscls texlive-anyfontsize texlive-cmap texlive-fancyhdr texlive-fncychap \
                   texlive-dvisvgm texlive-metafont texlive-ec texlive-titlesec texlive-babel-english texlive-tabulary \ 
                   texlive-framed texlive-wrapfig texlive-parskip texlive-upquote texlive-capt-of texlive-needspace \
                   texlive-times texlive-makeindex texlive-helvetic texlive-courier texlive-gsftopk texlive-dvips texlive-mfware texlive-dvisvgm && \
    pip3 install rst2pdf sphinx && \
    pip3 install git+https://github.com/esmci/sphinx_rtd_theme.git@version-dropdown-with-fixes && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf && \
    ldconfig && \
    yum clean all

# Set up the environment - create the group and user, the shell variables, the input data directory and sudo access:
RUN groupadd sphinx && \
    useradd -c 'Sphinx User' -d /home/user -g sphinx -m -s /bin/bash user && \
    echo 'export USER=$(whoami)' >> /etc/profile.d/sphinx.sh && \
    echo 'export PS1="[\u@sphinx \W]\$ "' >> /etc/profile.d/sphinx.sh && \
    echo 'user ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers.d/sphinx

ENV  SHELL=/bin/bash \
    LANG=C.UTF-8  \
    LC_ALL=C.UTF-8 

USER user
WORKDIR /home/user
ENTRYPOINT ["/bin/bash", "-l"]
