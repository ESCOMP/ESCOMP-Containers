ARG DOCKER_NAMESPACE=""

FROM ${DOCKER_NAMESPACE}/esmf

RUN pip3 install sphinx sphinxcontrib-packages sphinxcontrib-bibtex
RUN apt-get --yes update && apt-get --yes install latexmk texlive-fonts-recommended texlive-latex-recommended texlive-latex-extra
