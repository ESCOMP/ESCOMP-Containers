
Containerized versions of ESCOMP software (eg, CESM)

(This is currently in development; documentation and versions are likely to change rapidly.)



# Quick Start for CESM:

You need to mount a directory in to the container to save any files / inputdata - this is done via the '-v' option to 'docker'.  For example, to run an interactive bash shell with a local 'cesm' directory (/Users/me/cesm) mounted into home, do:

<i>docker run -it -v /Users/me/cesm:/home/user escomp/cesm-2.1</i>


NOTE: For systems with many cores, you might also need to use an option like --dev-shm=512M, since each MPI process will require some space in /dev/shm

(Unlike a CESM configuration on an HPC system, with dedicated directories for inputdata and scratch, this containerized version stores everything in the /home/user directory, so mounting a local directory ensures you'll not have to download input data multiple times, or lose run data.)

This will give you a bash prompt like this:

[user@cesm2.1.3 ~]$

From here, you can follow the standard CESM documentation on creating / building / submitting cases - in this case, the submission runs in the foreground.  An example set of commands to build a 2-degree F2000climo (scientifically unsupported, just used as an example) case, with a case name / directory of 'test1' follows:<br /><br />
<i>
create_newcase --case test1 --compset F2000climo --res f19_g17 --run-unsupported<br />
cd test1<br />
./xmlchange NTASKS=4 <br />
./case.setup <br />
./case.build <br />
./case.submit <br />
</i>

This will require ~7-10GB of RAM for 1-4 tasks - if you haven't configured your Docker environment to allow that, you'll need to change that under Docker's settings.

(These will change soon; this is just a is-it-working example.)
