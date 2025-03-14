![Graph of the sum, maximum, and minimum
of the performance of the TOP500 supercomputing sites
from 1993 to 2024.
The performance ranges from $10^9$ FLOP/s for the slowest system in 1993,
to over $10^{18}$ FLOP/s for the fastest system in 2024.](./images/top500.svg) <!-- .element width="1200px" -->

Data: [TOP500.org](https://top500.org)

Script:
The TOP500 supercomputing sites collates 
performance statistics on supercomputers around the world.
In the 2010s it was identified that on the then-present trajectory,
the fastest machines would start reaching an exaflop of performance,
that is,
$10^{18}$ floating point operations per second
on the benchmark problem used for this assessment,
in the next decade,
and that the slowest machines in the list,
which represent more typical academic clusters,
would reach that point in the following decade.
Since as we explored in a previous video,
the performance of individual execution units has stopped increasing significantly,
this started a lot of thinking about
what the technology to enable this would look like.
We refer to the set of technologies in this direction,
including both programming paradigms and hardware technologies,
"exascale".
This is to be inclusive of a lot of related challenges,
and not solely focused on the artificial number of FLOP/s on one benchmark.
As the plot shows,
the latest and greatest supercomputers can now reach the exascale;
however,
the effort required is collossal,
and the rate of speedup of commodity academic clusters has fallen significantly,
so these show no sign of operating at exascale in the immediate future.

-

1000$\times$

<div style="width: 100%">
<div class="fragment" style="width: 15%; display: inline-block;" data-fragment-index="1">Application</div>
<div class="fragment" style="width: 28%; display: inline-block;" data-fragment-index="1">

$V>256^4$

</div>
<div class="fragment" style="width: 28%; display: inline-block;" data-fragment-index="3">

$N_\beta$, $N_m\rightarrow \infty$

</div>
<div class="fragment" style="width: 25%; display: inline-block;" data-fragment-index="5">

LLR

</div>
</div>

<div style="width: 100%; margin-bottom: 50px;">
<div class="fragment" style="width: 15%; display: inline-block;" data-fragment-index="2">Challenge</div>
<div class="fragment" style="width: 28%; display: inline-block;" data-fragment-index="2">

$N_{\mathrm{proc}} \rightarrow O(10^5)$

</div>
<div class="fragment" style="width: 28%; display: inline-block;" data-fragment-index="4">

$N_{\mathrm{jobs}} \rightarrow \infty$

</div>
<div class="fragment" style="width: 25%; display: inline-block;" data-fragment-index="6">

Software maturity

</div>
</div>


Script:
Some discussions of exascale characterise it as
a hundred- or thousand-fold increase in performance over what is available "today",
for some value of today.
Since as we've discussed elsewhere,
the speed of single threads is not increasing substantially,
this performance boost comes from massive parallelism.
What does this mean for lattice?
Generally in lattice we already work at the limit of
where parallelism give s us increased performance
for a given problem.
As such,
exascale computing may not speed up existing computations;
however,
it can let us picture new studies that would not have previously been possible.
[click]
One route is to look at substantially larger lattices than we currently study.
For example,
some collaborations are now starting to look at volumes of $256^4$ and above.
The main requirement to enable this is to have
software that can scale to thousands or tens of thousands of processes
without sacrificing performance,
or introducing errors.
A second option is to generate more ensembles.
Whereas previously one may study a handful of masses
and one or two values of the gauge coupling,
exascale in principle allows for many values of each,
allowing for better understanding of the approach to the continuum and chiral limits.
This is particularly useful when exploring theories beyond the Standard Model,
where the physical parameters are not necessarily known up front.
The big software challenge here is
having tooling to manage the large number of individual parameter sets:
while for a handful of jobs it is feasible to monitor,
set parameters,
and re-launch failed jobs all by hand,
for a hundred or a thousand jobs this has to be automated to be viable.
Thirdly,
techniques can be used that run multiple coupled Markov chains in parallel;
this includes techniques like parallel tempering and the related LLR algorithm.
This uses strong scaling within each replica of the lattice,
but only needs a relatively small amount of bandwidth
to keep the replicas coupled to each other,
so can scale well to large processor counts.
These techniques can be used to overcome issues like topological freezing,
as well as probing new observables like the density of states.
A constraint here is the maturity of the software;
there is currently no feature-complete LLR implementation for
the Hybrid Monte Carlo with fermions.

-

![A clean white datacentre,
containing rows of racks,
the end of each of which is blue with 富岳 written in white](./images/fugaku.jpg) <!-- .element width="1300px" -->

Script:
A major difficulty of exascale computing is density,
both of compute units and the energy to power them.
Only one country has attempted to come close to exascale with a CPU-based machine;
this is Japan,
whose Supercomputer Fugaku is shown on screen.
As of November 2024,
this is the sixth-fastest machine in the world,
achieving over 400 teraflops at peak.
All other efforts in the exascale direction,
including Japan's planned successor to Fugaku,
are based on accelerators.
This allows the same computational capability to fit into a much smaller volume,
and consumes much less power.
Even for Fugaku,
custom-designed processors were needed to achieve better performance per watt,
and its total power draw is higher than El Capitan,
the current number one for performance.

-

![NVIDIA logo](./images/nvidia.svg) <!-- .element width="340px" style="margin: 40px; vertical-align: middle;" -->
![AMD logo](./images/amd.svg) <!-- .element width="300px" style="margin: 60px; vertical-align: middle;" -->
![Intel logo](./images/intel.svg)  <!-- .element width="240px" style="margin: 90px; vertical-align: middle;" -->

<div class="fragment" style="width: 420px; text-align: center; display: inline-block;">CUDA</div>
<div class="fragment" style="width: 420px; text-align: center; display: inline-block;"><span style="text-decoration: line-through;">OpenCL</span><br>HIP</div>
<div class="fragment" style="width: 420px; text-align: center; display: inline-block;">SYCL</div>

Script:
There is no one accelerator technology monopolising the exascale space.
Accelerators from NVIDIA, AMD, and Intel are all used.
[click]
NVIDIA has for a long time required
using their proprietary language CUDA to program their GPUs.
While recently they have begun to push for "standard language parallelism",
they admit that this does not give the same performance as writing directly in CUDA.
CUDA is based on C,
and can be used in C++;
there is also a Fortran variant available.
[click]
Historically,
AMD GPUs were programmable using OpenCL,
an open standard for GPU programming;
this was widely regarded as a cumbersome language to write
and difficult to get good performance with.
While it is still supported,
it is now encouraged to use the HIP language instead;
this is very closely-related to CUDA,
but with different keywords.
Automated translation from CUDA to HIP is frequently possible.
HIP's use outside of AMD GPUs is currently limited,
although in some cases it has been found to be faster than CUDA on NVIDIA hardware.
[click]
Intel have tried to drive a community initiative for
a set of open standards for cross-platform programming
for both accelerators and non-accelerated computation.
They have called this oneAPI,
and the language for writing software for their accelerators is called SYCL.
SYCL is based on C++17,
and is intended as a higher-level abstraction of OpenCL;
support for C and Fortran is limited.
As part of the Intel-driven community initiative,
SYCL is claimed to be supported on all three major accelerator vendors;
however,
its cross-compatibility and performance on non-Intel hardware is not fully proven,
and it doesn't get full support from NVIDIA or AMD.

-

```c
/* All changes must apply to all four versions! */
void dirac_operator_cuda(gauge_field_cuda* U, spinor_field_cuda* in, spinor_field_cuda* out);
void dirac_operator_cpu(gauge_field_cpu* U, spinor_field_cpu* in, spinor_field_cpu* out);
void dirac_operator_hip(gauge_field_hip* U, spinor_field_hip* in, spinor_field_hip* out);
void dirac_operator_sycl(gauge_field_sycl* U, spinor_field_sycl* in, spinor_field_sycl* out);
```

<!-- .element style="width: 1300px;" -->

Script:
In general,
we don't want to try to maintain
a complex codebase with multiple different programming paradigms throughout.
Having different versions of every function and datatype for every platform we're targeting
rapidly gets out of hand;
different versions of the functions develop different features and limitations,
meaning you lose confidence in whether you can run a given problem or not.
So how can we have maintainable software that is performant on all exascale hardware?

-

```c
#ifdef CUDA
#include "cuda_primitives.h"
#endif
...
void dirac_operator(gauge_field* U, spinor_field* in, spinor_field* out);
```

Script:
One way to approach this is using "separation of concerns".
You design your software such that it has a split between
code that deals with the physics of interest,
and code that deals with talking to the device
(sometimes called a backend),
and have a well-defined interface between them.
This way,
you quarantine all of the device-specific code into a small module.
When you need to support a new accelerator technology,
you can add a new backend for it,
without needing to go through and edit every single file in the codebase.

-

[![Alpaka](./images/alpaka.svg) <!-- .element width="400px" style="margin: 50px; vertical-align: middle;" -->](https://alpaka.readthedocs.io/en/stable/)
[![Kokkos](./images/kokkos.svg) <!-- .element width="400px" style="margin: 50px; vertical-align: middle;" -->](https://kokkos.org)

[![RAJA](./images/raja.svg) <!-- .element width="400px" style="margin: 50px; vertical-align: middle;" -->](https://github.com/llnl/RAJA)
[![SYCL](./images/sycl.svg) <!-- .element width="400px" style="margin: 50px; vertical-align: middle;" -->](https://sycl.tech)

Script:
The other way to do this is,
effectively,
to outsource the separation of concerns to someone else,
by using a performance portability library.
The most commonly used of these are alpaka,
Kokkos,
RAJA,
and SYCL.
All of these are C++-based,
and each has slight differences but aims to achieve broadly the same thing:
allowing you to write code that can be compiled for CPU,
or for GPUs from multiple vendors,
and get good performance on all of them.
