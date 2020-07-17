
Containerized versions of ESCOMP software (eg, CESM)

(This is currently in development; documentation and versions are likely to change rapidly.)



# Quick Start for CESM:

You need to mount a directory in to the container to save any files / inputdata - this is done via the '-v' option to 'docker'.  For example, to run an interactive bash shell with a local 'cesm' directory (/Users/me/cesm) mounted into home, do:

<i>docker run -it -v /Users/me/cesm:/home/user escomp/cesm-2.1</i>


(Unlike a CESM configuration on an HPC system, with dedicated directories for inputdata and scratch, this containerized version stores everything in the /home/user directory, so mounting a local directory ensures you'll not have to download input data multiple times, or lose run data.)

This will give you a bash prompt like this:

[user@cesm2.1.3 ~]$

From here, you can follow the standard CESM documentation on creating / building / submitting cases - in this case, the submission runs in the foreground.  An example set of commands to build a 2-degree F2000climo (scientifically unsupported, just used as an example) case, with a case name / directory of 'test1' follows:

% create_newcase --case test1 --compset F2000climo --res f19_g17 --run-unsupported
% cd test1
% ./xmlchange NTASKS=1
% ./case.setup
% ./case.build
% ./case.submit

(These will change soon; this is just a is-it-working example.)
