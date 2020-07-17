
Containerized versions of ESCOMP software (eg, CESM)

(This is currently in development; documentation and versions are likely to change rapidly.)



# Quick Start for CESM:

You need to mount a directory in to the container to save any files / inputdata - this is done via the '-v' option to 'docker'.  For example, to run an interactive bash shell with a local 'cesm' directory (/Users/me/cesm) mounted into home, do:

<i>docker run -it -v /Users/me/cesm:/home/user escomp/cesm-2.1</i>

Unlike a CESM configuration on an HPC system, with dedicated directories for inputdata and scratch, this containerized version stores everything in the /home/user directory, so mounting a local directory ensures you'll not have to download input data multiple times, or lose run data. 
