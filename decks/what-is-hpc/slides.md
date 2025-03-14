<div style="float: left; width: 30;">

![An illustration of a lattice](images/lattice.svg) <!-- .element width="100%" -->

</div>

<div style="float: right; width: 69%;">

- &shy;<!-- .element: class="fragment" --> $128\times64^3=$ 33,554,432 sites
- &shy;<!-- .element: class="fragment" --> $\times 4=$ 134,217,728 links
- &shy;<!-- .element: class="fragment" --> $\times 3\times3=$ 1,207,959,552 complex numbers
- &shy;<!-- .element: class="fragment" --> $\times 2=$ 2,415,919,104 real numbers
- &shy;<!-- .element: class="fragment" --> $\times 100\times 100=$ 24,159,191,040,000 matrix-vector multiplications
- &shy;<!-- .element: class="fragment" --> $\times 100=$ 2,415,919,104,000,000 floating-point operations per update
- &shy;<!-- .element: class="fragment" --> $/(8\times 4\times10^9 \mathrm{s}^{-1}\times 12)=$ 6,291 s
- &shy;<!-- .element: class="fragment" --> $\times 1000\times4=$ 25,165,824 s
- &shy;<!-- .element: class="fragment" --> $\equiv$ 291 days

</div>

Script:
[click]
A lattice of size 128 by 64 cubed has
[click]
134 million links.
If we're looking at the SU(3) gauge group,
[click]
this is 1.2 billion complex numbers,
[click]
or over 2.4 billion real numbers.
Assuming we are generating configurations with the Hybrid Monte Carlo,
each trajectory involves a few dozen steps,
each of which requires an inversion of the Dirac operator,
requiring at least a few dozen matrix-vector multiplications,
each of which might need to perform a hundred floating point operations on each number.
This means each update has of the order of
quadrillions of floating point operations.
(For fermion formulations with additional dimensions,
such as Domain Wall Fermions,
this explodes further.)
In double precision,
with eight bytes per real number,
we require tens of gigabytes of memory.
A typical desktop CPU might have 8 CPU cores,
each of which runs at a frequency of around 4GHz,
and be able to run a dozen or so instructions on each clock cycle,
so with perfectly efficient software,
[click]
a single trajectory may require around two hours.
Bear in mind that to get good statistics
we may require a thousand or more configurations,
each decorrelated by four or more trajectories,
[click]
and we see that we need the better part of a year to generate this ensemble.
We typically need more than one ensemble,
to understand how our results depend on one or more of the input parameters,
so this multiplies up into a very long time to keep a computer busy.

-

![A laptop](./images/laptop.svg) <!-- .element width="150px" -->

![A laptop with a fast-forward icon](./images/laptop-go-fast.svg) <!-- .element width="150px" class="fragment" style="margin: 40px" --> ![Three laptops with different beta values assigned to each](./images/three-laptops-different.svg) <!-- .element width="450px" class="fragment" style="margin: 40px" --> ![Three laptops connected together, with the same beta value assigned to each](./images/three-laptops-collaborate.svg) <!-- .element width="450px" class="fragment" style="margin: 40px" --> 

Script:
We generally need to get results on timescales shorter than decades,
so we need a way to do this work faster.
One way to do this is to improve our algorithms,
so that there are fewer operations to do.
There has already been a lot of work there though,
so getting further reductions could be an entire career in itself.
That limits us to getting the same operations done,
in less time.
[click]
One way to do this is to make the CPU in the computer do each instruction more quickly.
Until the early 2000s,
this was a reliable way to get faster results:
wait until a faster chip came out.
Unfortunately,
after that point we started to hit the limit of how fast a single thread can go;
advancements since then have been in getting more things done at once.
Remember that our HMC algorithm is a Markov chain;
we cannot generate the next state until the current one is complete,
so we cannot trivially parallelise over Monte Carlo iterations.
[click]
Another way to get more done
is to run multiple different tasks in parallel.
For example,
if we are studying multiple values of $\beta$,
we can use one computer for each of them.
To a certain extent,
we can do this for Markov chains too:
we can take a thermalised state,
and start a second or third Markov chain with a new random seed,
letting us use two or three computers at once rather than one.
Based on what we discussed on the previous slide,
that could still require a year or more to generate a single ensemble.
What if that's simply too long?
[click]
The third option is to have multiple computers collaborate on the same problem.
Some element of this is necessary even within one computer.
You might have noticed I mentioned using 8 CPU cores;
each of these operates independently,
so the programmer needs to work to let all cores collaborate on the same problem.
The same can apply across multiple computers.

-

![A supercomputer](./images/supercomputer.jpg) <!-- .element width="1200px" -->

Script:
Now,
if we are going to be spreading our work across many computers,
there are some things we can do to make life easier.
Firstly,
we don't really need a screen,
keyboard,
or mouse for every single one;
better to save that cost so we can afford more computers instead.
Rather than scattering them across the office,
we can put them in a dedicated room,
that can be temperature controlled to stop the computers overheating.
We can build them into a standardised shape,
so they can more easily fit together.
Because they're in their own room with temperature control and good electrical supply,
we can fit more CPU cores and more memory into each computer,
reducing the number of computers we need for a given problem.
We can also add specialised high-speed networking between them,
so that when collaborating on a single problem,
there is less slowdown due to waiting for communications between each other.
Perhaps we will also add accelerators,
like GPUs,
that can do far more instructions at the same time than a typical CPU,
with lower power consumption,
albeit with less flexibility on how those instructions are programmed.
We call a facility built this way,
in a dedicated datacentre,
with a high-speed network fabric and using powerful computers,
a "supercomputer",
or a "high-performance computing cluster",
and the individual computers forming it,
"nodes".
You might also come across the word "exascale";
this refers to the highest-end supercomputers
that can run in the region of $10^{18}$ floating point operations per second
(an exaflop);
as of November 2024,
there are three machines in the world meeting this criterion:
El Capitan,
Frontier,
and Aurora,
all based at United States national laboratories.

-

![Diagram showing compute jobs arranged into a 2D timeline,
with time on the horizontal axis,
and nodes on the vertical axis.](./images/scheduling.svg) <!-- .element width="1200px" -->

Script:
HPC machines are pretty costly to buy and run,
typically millions of pounds, dollars, or Euro for a modestly sized one,
up to billions for the largest exascale facilities.
Because of this,
you're very unlikely to have one all to yourself,
both because you likely don't have that level of funding,
but also because one person 
is unlikely to be able to keep the machine busy for 100% of the time.
The funders' money is better spent on a shared machine,
where multiple people submit work,
that between all users keeps the machine busy.
Depending on the funding,
this may be specific to lattice,
or it may be shared among multiple research fields.
To make sure that everyone gets their fair share of the resource,
and doesn't trample over other users' work,
machine use a "resource manager" or "job scheduler"
to decide what software runs when.
The most common way such schedulers work
is that you give them a shell script to run,
encoding into it what resources it needs,
and then the scheduler will hold it until the resources are available,
and then start the work.
Since this might happen hours or days later,
at the weekend or the middle of the night,
it's important that the work you want to run is automated.

-

![Diagram showing Tanaka Tarou at pylaptop42
connecting to pycluster with user ttanaka,
but with a golden wall and a lock icon in the way.](./images/secure-hpc.svg) <!-- .element width="1200px" -->

Script:
Due to their cost,
size,
and specific environmental needs,
HPC machines are typically kept in locked datacentres,
where only authorised administrators have the keys.
Occasionally you might be taken on a guided tour to see the machine,
but it's very unlikely you'll walk up to the machine to give it your workloads.
Instead,
jobs are submitted to HPC facilities over the Internet or local network,
connecting via the Secure SHell protocol SSH.

-

![Diagram showing a user connecting to a cluster,
which is broken down into a gateway node,
two login nodes,
a management node,
a high-speed switch,
six CPU nodes,
six GPU nodes,
and a storage array,
with most components connected to the high-speed switch.](./images/cluster-structure.svg) <!-- .element height="700px" -->

Script:
A typical cluster will have most of the components shown here.
As a user,
you will connect via the Internet or a local network to a login node.
(There will frequently be more than login node available,
but usually you don't need to care about this;
you will be directed to one of them automatically.)
The work will be performed by compute nodes.
If there is more than one type of compute nodes
(for example,
with and without GPUs,
or some with extra memory),
then these will be in different "partitions" or "queues".
You don't connect to these nodes directly,
but instead ask the scheduler to run work for you.
There will be some shared storage,
which may be one large filesystems,
or may be split into filesystems for your home directory,
storage for larger working data,
high-speed scratch storage,
etc.
This storage will be accessible both to the login nodes,
and to the compute nodes.
All nodes will connect to a high-performance network "fabric" switch,
which is used for low-latency, high-bandwidth communications
when a parallel problem is being worked on,
and for connecting to the storage.
Separately,
all nodes will also connect to a slower network used for management;
for example,
telling the nodes which work to run.
The login nodes are usually able to access the Internet,
but frequently compute nodes are not.
On such machines,
if you're working on code that needs to download data,
it's best if you can pre-fetch the necessary files from the login node
before starting your job.

-

![A cloud](./images/cloud.svg) <!-- .element width="700px" -->

Script:
You might have heard of the idea of "the cloud"
as a computing resource.
This has some similarities with HPC,
but some differences as well.
Let's compare and contrast them now.

-

![Photograph of a datacenter](./images/datacentre.jpg) <!-- .element height="700px" -->

Script:
Both HPC and cloud computing resources are made up of
a bunch of servers sitting in a datacenter somewhere.

-

![Diagram showing compute jobs arranged into a 2D timeline,
with time on the horizontal axis,
and nodes on the vertical axis.](./images/scheduling.svg) <!-- .element width="1200px" -->

Script:
Both HPC and cloud computing resources will have
the same hardware being used by different people at different times.

-

![Illustration showing a queue of stick figures waiting for a door marked "HPC",
and an empty door marked "Cloud"](./images/queue.svg) <!-- .element height="600px" -->

Script:
Cloud services are designed so that when you ask for a resource,
you get it straight away.
This is important when you're running a business,
and you have a spike in load meaning you need more resources right now,
but does mean that clouds have to have large amounts of resources sitting idle,
just in case a spike in load occurs.
HPC systems are generally set up to maximise the amount of output
for the resources invested in buying them;
this means that they are generally filled,
so you need to wait in a queue for your work to start.

-

![Illustration of a balance,
with a few banknotes on the side labeled HPC,
and many banknotes on the side labeled Cloud.](./images/cloud-cost.svg) <!-- .element height="600px" -->

Script:
Because of this,
if you have enough work to keep it busy all the time
(as is usually the case in lattice),
and run it for more than a year or two
(which is almost always the case),
an HPC system is typically significantly cheaper than
buying equivalent services from a cloud provider.
On top of this,
frequently in academia access to HPC is gained through grants of computing time,
rather than buying time,
so the direct cost is effectively zero.

-

![Illustration of shop windows,
showing two shades of T-shirts available from the HPC shop,
but a rainbow of colours in the Cloud shop.](./images/hpc-cloud-choice.svg) <!-- .element height="600px" -->

Script:
That said,
because of their scale,
cloud providers can offer a much wider choice of hardware than most HPC centres,
where the hardware is designed around the typical use case of the facility.
If you need much less power than a typical HPC node provides,
and you would need to pay the HPC centre for the full node resource,
you may be better off running in the cloud on resources that are a better fit.
If you need to get brief access to specific hardware
that it doesn't make sense for you to buy,
for example to benchmark new hardware,
using the cloud makes a lot of sense.
Or if you need to use hardware for a few hours a week,
that will remain idle the rest of the time,
it's worth checking whether you could make use of a cloud service.

-

![Illustration of a lock](./images/lock.svg) <!-- .element height="400px" -->

Script:
While it doesn't typically apply to lattice problems,
where we compile our software ourselves,
it's worth being aware that while on cloud systems
you generally get root (or administrator) access,
and can make any system modifications you like,
this is not usually the case on HPC clusters,
where you can only make changes in your own user or project space,
and need to open a support ticket for any actions that require elevated permissions.

-

![Icon representing a Unix shell](./images/shell.svg) <!-- .element height="400px" -->

Script:
I mentioned earlier that access to HPC is usually via a secure shell,
and that we represent the work to be done as a shell scripts.
The shell is a text-based way of interacting with a computer.
This pre-dates the graphical interfaces you are likely more familiar with,
but in many ways is more powerful,
and is better suited both to interacting with a remote computer,
and to encoding the work that we want to do in a form to give to a scheduler.
The command prompt `cmd.exe` on Windows is one example,
but in academia there are no supercomputers that run Windows.
Instead,
we make use of the Unix shell.
If you're not already familiar with the Unix shell,
we'd strongly recommend working through the
[Software Carpentry Introduction to the Unix Shell][shell-novice]
before continuing this track.
Once you've done that,
we'll talk about how to get started using HPC,
and some of the specific things to think about when running lattice work on a cluster.

[shell-novice]: https://swcarpentry.github.io/shell-novice
