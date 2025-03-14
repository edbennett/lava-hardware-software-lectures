![Diagram of a flowchart of routes from "Start" to "Cluster access",
with varying levels of complexity](./images/access-flows.svg) <!-- .element width="1200px" -->

Script:
So,
you've reached the point where your laptop is no longer enough,
and you need access to high-performance computing.
The first step is to identify what facility you can get access to,
and follow the procedure for accessing it.
These are questions we can't answer generically here;
your supervisor or a more senior colleague will likely know
what resources are available in your institution and country.
Depending on the size of the resource,
getting access might be a matter of asking the administrator to create you account,
filling out some web forms to request an account and a project code,
or doing a series of fetch quests like a protagonist in a role-playing game.
Whatever happens,
once you've done this,
you probably have a username,
and either a password or a key to log in to the machine.

-

<div style="float: left; margin: 40px;">

Scheduler:

- PBS Pro
- Slurm
- PJM
- LFS/Spectrum Symphony
- SGE
- ...

</div>
<div style="float: left; margin: 40px;">

Vendor:

- HPE/Cray
- Eviden/Bull
- Dell
- Fujitsu
- NEC
- ...

</div>
<div style="float: left; margin: 40px;">

Filesystem:

- GPFS/Storage Scale
- Lustre
- BeeGFS

</div>

Script:
For the rest of this video,
we'll look at how to set up your workload on a generic cluster.
Of course,
no cluster is truly generic,
so you should follow this material
in conjunction with reading the documentation from your HPC centre,
if it exists.
If things are unclear,
don't be afraid to reach out to your local support team for help.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">ssh username@my.hpc.system</span>
<br>
<span class="fragment">
The authenticity of host 'my.hpc.system (198.51.100.23)' can't be established.<br>
ED25519 key fingerprint is SHA256:gVgjfMMsHH10tt0nT5CKtYCqSaVRIVgK7NpA09QW4NB.<br>
This key is not known by any other names.<br>
Are you sure you want to continue connecting (yes/no/[fingerprint])? 
</span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">yes<br></span>
<span class="fragment">
Warning: Permanently added 'aluminiumdreams' (ED25519) to the list of known hosts.<br>
Password:<br>
</span>
<span class="fragment">
Your password has expired and must be changed.<br>
Current password:<br>
</span>
<span class="fragment">
Password:<br>
</span>
<span class="fragment">
Repeat password:<br>
</span>
<span class="fragment">
All authentication tokens were updated successfully<br>
$
</span>
</div>


Script:
Let's assume for now that you have a username and a password,
and have found out the address you need to connect to
from the documentation for the system you are using.
In a new terminal,
run the command
[click]
ssh your username, at sign, the address to connect to.
This will work at the shell in Linux or macOS,
and in the Command Prompt on Windows.
The first time you connect,
[click]
`ssh` will prompt you to confirm that the machine you're connecting to is right.
If you're paranoid,
you can verify the fingerprint with the administrators,
but most people will type `yes` at this point to continue.
(Note that you do need to type the whole word here.)
[click]
Next,
you'll be prompted for your password.
Nothing will appear on screen while you're typing it,
but press Enter once you have finished and it will be verified by the cluster.
Some machines either allow or require an SSH key instead of or as well as your password;
we'll talk about this in another video.
Other machines might ask for a two-factor authentication code at this point;
this differs for each machine,
so please look at the documentation for your machine
to understand how to set up and use 2FA.
The first time you log in,
and at regular intervals afterwards,
[click]
you might be prompted to change your password.
Some systems do this on the web via a portal,
while others do it at the terminal.
If you're prompted,
then you will need to enter your current password,
[click]
then enter your new password twice,
[click]
pressing enter after each time.
As before,
nothing shows on the screen while you're typing your passwords.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">pwd</span><br>
<span class="fragment">/lustre/home/username<br>$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">ls -d /data/${USER} /scratch/${USER}
</span><br>
<span class="fragment">/data/username /scratch/username<br>$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">lfs quota -u $(id -u) . -h</span><br>
<span class="fragment">Disk quotas for usr 20683 (uid 20683):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Filesystem&nbsp;&nbsp;&nbsp;&nbsp;used&nbsp;&nbsp;&nbsp;quota&nbsp;&nbsp;&nbsp;limit&nbsp;&nbsp;&nbsp;grace&nbsp;&nbsp;&nbsp;files&nbsp;&nbsp;&nbsp;quota&nbsp;&nbsp;&nbsp;limit&nbsp;&nbsp;&nbsp;grace<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;12.24T&nbsp;&nbsp;24.50T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;25T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8288;—&#8288;&nbsp;&nbsp;990332&nbsp;1950000&nbsp;2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-<br>$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">lfs quota -g $(id -g) . -h</span>
<span class="fragment">Disk quotas for grp 20288 (gid 20288):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Filesystem&nbsp;&nbsp;&nbsp;&nbsp;used&nbsp;&nbsp;&nbsp;quota&nbsp;&nbsp;&nbsp;limit&nbsp;&nbsp;&nbsp;grace&nbsp;&nbsp;&nbsp;files&nbsp;&nbsp;&nbsp;quota&nbsp;&nbsp;&nbsp;limit&nbsp;&nbsp;&nbsp;grace<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.&nbsp;&nbsp;61.29T&nbsp;&nbsp;72.50T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;73T&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8288;—&#8288;&nbsp;2177482&nbsp;4500000&nbsp;5000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-<br>$&nbsp;</span>
</div>

Script:
Once were logged in,
we want to know where to put our stuff.
You almost certainly will have a home directory,
and since logging in will start you in your home directory,
[click]
`pwd` will tell you where that is.
[click]
Depending on the setup of the machine,
you may also have other storage available.
On some machines,
your home directory is slow to access,
and should not be used for your main production work.
There may be higher-speed
[click] [click]
(frequently under `/data`)
or ephemeral
(sometimes under `/scratch`)
storage that is designed for more heavy usage.
Your system's documentation should tell you more about this.
You almost have a quota applied,
either to the files you own on the system,
or the files owned by the project you are a part of.
The command to check this varies from system to system;
consult the documentation to see how the service you're using recommends
checking the quota on the system you're using.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">git clone https://github.com/-an--author-/AwesomeLat</span><br>
<span class="fragment">
Cloning into 'AwesomeLat'...<br>
remote: Enumerating objects: 732, done.<br>
remote: Counting objects: 100% (167/167), done.<br>
remote: Compressing objects: 100% (119/119), done.<br>
remote: Total 732 (delta 93), reused 105 (delta 48), pack-reused 565 (from 1)<br>
Receiving objects: 100% (732/732), 41.17 MiB | 8.49 MiB/s, done.<br>
Resolving deltas: 100% (320/320), done.<br>
$ </span>
</div>

Script:
Once we know where to put things,
we can move on to getting our software set up.
Typically,
when starting working on a new machine,
we'll need to install the lattice-specific software we'll be using.
Because HPC systems are shared machines,
we typically won't have root access,
so will need to do all installations in our home directory.
For lattice software,
this typically isn't a problem,
since it's designed to be run on supercomputers,
so doesn't require any modifications needing root.
[click]
`git` is typically installed by default,
[click]
so you can clone your code from a central repository.

-

<div class="code">
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">module available</span><br>
<span class="fragment">
&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&nbsp;/lustre/apps/cuda&#8288;—&#8288;12.3&#8288;—&#8288;modulefiles&nbsp;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;<br>
cuda/12.3&nbsp;&nbsp;openmpi/4.1.5&#8288;—&#8288;cuda12.3&nbsp;&nbsp;ucx/1.15.0&#8288;—&#8288;cuda12.3<br>
<br>
&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&nbsp;/lustre/apps/cuda&#8288;—&#8288;11.4.1&#8288;—&#8288;modulefiles&nbsp;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;<br>
cuda/11.4.1&nbsp;&nbsp;openmpi/4.1.1&#8288;—&#8288;cuda11.4.1&nbsp;&nbsp;ucx/1.12.0&#8288;—&#8288;cuda11.4.1<br>
<br>
&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&nbsp;/lustre/apps/modulefiles&nbsp;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;&#8288;—&#8288;<br>
cuda/11.0.3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;module-git&nbsp;&nbsp;&nbsp;null&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ucx/1.10.1<br>
dot&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;module-info&nbsp;&nbsp;openmpi/4.0.4&nbsp;&nbsp;use.own<br>
gcc/9.3.0(default)&nbsp;&nbsp;modules&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;openmpi/4.1.1&nbsp;&nbsp;xpmem/2.6.5<br>
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">module available 2&gt;&amp;1 | grep -i gcc</span><br>
<span class="fragment">
gcc/9.3.0(default)  modules      openmpi/4.1.1  xpmem/2.6.5<br>
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">module load gcc/9.3.0 openmpi/4.1.1</span><br>
<span class="fragment">$ </span>
</div>

Script:
You'll most likely need to compile your code before you can run it.
If you're using an interpreted language,
then you'll instead need access to an interpreter.
Either way,
you will need a specific piece of software.
Since HPC centres need to support many users with diverse needs,
supercomputers typically have a wide range of software and software versions available.
However,
having multiple versions of many programs will typically cause conflicts between them,
so none are available by default.
Instead,
software is provided as "modules",
which must be loaded as they are needed.
To see what's available,
we can use the `module available` command.
Because the `module` command outputs to the error stream,
if we want to use `grep` to find a module,
we need to redirect the error stream.
Once we have found a module we want to activate,
we can do this with the `module load` command.

-

![A graph showing very different performance characteristics for different compiler choices](./images/compiler-choice.svg) <!-- .element height="600px" -->

Script:
You should test a range of the compiler and MPI versions available
to see which performs best for your code on the specific machine you're using.
Sometimes different versions are particularly well-tuned for a given machine,
and can give substantial performance boosts.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">make install</span><br>
<span class="fragment">Permission denied<br>
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">../configure --prefix=${HOME}/prefix-awesomelat</span>
<br>
<span class="fragment">...</span>
</div>

Script:
From here,
we can configure and build our software as normal.
Since we don't have root access,
we can't use `make install` as-is,
if that's something you would usually do.
However,
if we pass a `--prefix` option to the configure script
(or equivalent in your build system),
we can tell the installer to place the installed program in our home directory,
or some other directory we have write access to,
rather than in the protected common operating system location.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">sinfo</span><br>
<span class="fragment">
PARTITION&nbsp;&nbsp;&nbsp;AVAIL&nbsp;&nbsp;TIMELIMIT&nbsp;&nbsp;NODES&nbsp;&nbsp;STATE&nbsp;NODELIST
cpu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;up&nbsp;2&#8288;—&#8288;00:00:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;alloc&nbsp;cnode[1&#8288;—&#8288;10],[14&#8288;—&#8288;16]<br>
cpu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;up&nbsp;2&#8288;—&#8288;00:00:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;idle&nbsp;cnode[11&#8288;—&#8288;13]<br>
gpu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;up&nbsp;2&#8288;—&#8288;00:00:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;15&nbsp;&nbsp;alloc&nbsp;gnode[1&#8288;—&#8288;8,10,13&#8288;—&#8288;18]<br>
gpu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;up&nbsp;2&#8288;—&#8288;00:00:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;idle&nbsp;gnode[11&#8288;—&#8288;12]<br>
gpu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;up&nbsp;2&#8288;—&#8288;00:00:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;down&nbsp;gnode9<br>
$ </span>
</div>

Script:
Now we’re ready to start interacting with the job scheduler.
Currently the most common scheduler on academic HPC systems is Slurm,
so we’ll use that as an example,
but all follow similar principles.
First up,
we can see what resources
(partitions, or queues)
are available and how busy they are;
in Slurm,
this is done with the `sinfo` command.
For example,
here we see that we have two partitions,
one for CPU-only jobs with 16 nodes,
and one with GPUs having 18 nodes.
Both impose a time limit of 2 days on jobs,
and each has a couple of nodes currently available.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">squeue</span><br>
<span class="fragment">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JOBID&nbsp;PARTITION&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;USER&nbsp;ST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIME&nbsp;&nbsp;NODES&nbsp;NODELIST(REASON)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10148&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu&nbsp;benchmar&nbsp;anothe01&nbsp;&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;33:27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;node004<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10145&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gpu&nbsp;spectrum&nbsp;jjones03&nbsp;PD&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16&nbsp;(Resources)<br>
...<br>
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">squeue --me</span><br>
<span class="fragment">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JOBID&nbsp;PARTITION&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;USER&nbsp;ST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIME&nbsp;&nbsp;NODES&nbsp;NODELIST(REASON)<br>
$ </span>
</div>

Script:
To see what jobs are running and waiting to be run,
in Slurm we can use the `squeue` command.
Some systems will only let you see your own jobs,
while others will show all users’.
The listing of all users' jobs can be very long;
in Slurm you can restrict the listing to just your jobs by adding the `--me` option.
Other schedulers will have similar options.
Since you haven't submitted a job yet,
you'll see just the header in the output of this command.

-

<div class="code">
<span class="fragment">#!/bin/bash</span><br>
<span class="fragment">#SBATCH --time 2:00:00</span><br>
<span class="fragment">#SBATCH --account project007</span><br>
<span class="fragment">#SBATCH --nodes 2</span><br>
<span class="fragment">#SBATCH --ntasks-per-node 8</span><br>
<span class="fragment">#SBATCH --cpus-per-task 16</span><br>
<span class="fragment">#SBATCH --output hmc.%J.out
<p>&nbsp;</span><br>
<span class="fragment">module purge</span><br>
<span class="fragment">module load gcc/9.3.0 openmpi/4.1.1</span><br>
<span class="fragment">${HOME}/src/awesomelat/build/hmc -i input_file</span>
</div>

Script:
Speaking of submitting a job,
now is a good time to start writing one.
A job script is a specially-formatted shell script,
with two parts.
Firstly,
there is a block of comments,
containing directives to the scheduler telling it more detail about your job.
After an instruction on which interpreter to use
[click]
(sometimes called a "shebang"),
each directive should start `#SBATCH`,
followed by an option
that could be passed as a command-line option to the `sbatch` command.
You should set a time limit a little above what you need for a given job
[click]
You also need to say what resources you need,
for example,
[click]
the number of nodes,
[click]
number of tasks per node,
[click]
and number of CPUs per task.
We'll talk more about tuning these in another video.
You can also specify where Slurm should put the output of the program.
The `%J` here means to include the job identifier in the filename,
so if you submit the job a second time,
the first output isn't overwritten.
[click]
After this part comes a list of commands  you want the job to perform,
in order.
To start off,
you should reload the modules you used to build your software,
[click] [click]
as frequently these provide libraries needed at run time.
Then,
the program that you want to run.
If you're using MPI,
some machines require you to use `srun` for this rather than `mpirun` or similar.
Either way,
you usually don't need to re-specify arguments like task or node count,
as the scheduler is able to provide this information to the MPI library directly.

-

<div class="code">
$
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">sbatch submit.sh</span><br>
<span class="fragment">Submitted batch job 10184<br>$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">squeue --me</span><br>
<span class="fragment">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JOBID&nbsp;PARTITION&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;USER&nbsp;ST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TIME&nbsp;&nbsp;NODES&nbsp;NODELIST(REASON)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10184&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu&nbsp;submit.s&nbsp;username&nbsp;PD&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;(Resources)<br>
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">squeue --me --start</span><br>
<span class="fragment">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;JOBID&nbsp;PARTITION&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;USER&nbsp;ST&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;START_TIME&nbsp;&nbsp;NODES&nbsp;SCHEDNODES&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NODELIST(REASON)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10184&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cpu&nbsp;submit.s&nbsp;username&nbsp;PD&nbsp;2025&#8288;—&#8288;03&#8288;—&#8288;04T02:58:00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;cnode[3,8]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Priority)<br>
$ </span>
</div>

Script:
We're now ready to submit this script to the scheduler,
which in Slurm we do with the `sbatch` command,
[click]
followed by the filename of the job script.
[click]
We can check the status of the job in the queue,
again using the `squeue` command.
[click] [click]
If there aren’t enough resources to start it straight away
(because they are running other jobs,
or are reserved for jobs already waiting to start),
then the job will wait until the resources become available.
The scheduler might give you a projected start time based on jobs currently in the queue;
for example,
by using the `--start` option to `squeue` in Slurm.
Note that this is an estimate,
and can change if other users submit jobs,
and in busy queues some jobs may not get an estimate straight away.

-

<div class="code">
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">tail hmc.10184.out</span><br>
<span class="fragment">
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 30 ; 30<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 21 ; 21<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 30 ; 30<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 9 ; 24<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 30 ; 30<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 21 ; 21<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 29 ; 29<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 20 ; 20<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 28 ; 28<br>
[INVERTER][10]g5QMR_mshift: cgiter (mshift,tot) = 21 ; 21<br>
$ </span>
<span class="fragment animate__fadeIn animate__faster" data-split="letters" data-delay="40" data-container-delay="0">scancel 10184</span><br>
<span class="fragment">$ </span>
</div>

Script:
Once your job starts running,
it will start writing its output to the output file you specified in the job script,
and you can look at these files to judge its progress.
If something goes wrong with a job,
like we have forgotten to specify a particular parameter,
we can cancel the job using the `scancel` command;
we don't need to wait for the job to complete or time out.

-

![An alarm clock](./images/alarm-clock.svg) <!-- .element class="fragment" height="100px" -->

<div class="code">
<span class="fragment">$ sbatch --dependency=singleton --array=1-10 submit.sh</span>
</div>

<div class="code" style="margin-top: 50px;">
<span class="fragment">$ tail -n 1 submit.sh<br>
srun ${HOME}/src/awesomelat/build/hmc && sbatch submit.sh</span>
</div>

Script:
Most HPC systems have a relatively short time limit
on how long a job can run for uninterrupted.
This is usually much shorter than
the time to get a complete set of Monte Carlo statistics for an ensemble.
There are a few ways we can deal with this.
[click]
One option is to log in every few days to check whether one has finished,
and resubmit manually.
[click]
Another option is to use the `--dependency=singleton` option
to only allow one job of a given name to run at a time,
and submit multiple copies,
for example using the `--array` option.
This way,
you don't have to log in to resubmit as frequently.
A third option,
if you HPC system allows it,
is to have the job resubmit itself.
After the command to to the data generation or analysis we are performing,
we can add the `&&` symbol,
followed by an `sbatch` command.
The `&&` means that the `sbatch` only runs if the previous command succeeds.
You do need to make sure that your software returns an error code if it fails
for this to work,
otherwise you'll create an infinite loop of unsuccessful jobs resubmitting themselves.
It will also only work correctly
if the job is able to finish its work in the available time,
so you will need
to tune the number of trajectories to complete in the specified time limit.

-

![Photograph of people in a training room](./images/training.jpg) <!-- .element height="600px" -->

Script:
We've had a whistle-stop tour of how to connect to and run your first job on HPC.
In later videos
we'll go into more detail on how to tune some of the options we've discussed.
In addition to the slides presented here,
we'd recommend going to any courses offered by the HPC centre you're using,
which will be more targeted to the actual machine you will be running on,
and will be able to answer your questions in more detail.
