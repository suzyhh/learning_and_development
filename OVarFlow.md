# OVarFlow: a resource optimized GATK4 based open source variant calling workflow
## Bathke and Luhken., 2021, bioRxiv

### Background
- GATK Best Practices when cited in literature do not always accurately represent the *actual* best practices workflow and often "diverge significantly from [GATK's] recommendations".
- This obscures the reproducability of methodolgies.
- OVarFlow is an open source, optimised, highly automated and reproducible workflow desgigned to combat these issues.

### Implementation
- The workflow consists of two phases:
    1. Basic variant calling workflow
    2. Optional extended workflow which allows further refinement using BQSR
- Controlled through Snakemake

#### Optimised parallelisation 
- Parallelisation is necessary to reduce processing time and workflows can be parallelised by at the process-level (e.g. process many individuals in parallel)
- bwa mem is set to use 6 threads by default in OVarFlow
- OVarFlow parallelises HaplotypeCaller by splitting the reference into several interals and processeing these as a scatter-gather. The default is four intervals.
- They also looked into paitMM threads in aplotypeCaller and set the default o 4, although this is a trade-off, as more processes can be run in parallel when only a single pairHMM thread is used.
- OVarFlow checks to see if AVX is available (it mostly is in newer CPUs)
- Java options are also configurable through the JVM. Java heap size and numer of garbage collection threads have substantial influence on performance of GATK tools.
- MarkDuplicates can be problematic as the tool open many files, this is a particular issue when mulitple instances of the tool are run in parallel. OVarFlow limits the number of file handles allowed by MarkDplicates

#### Configuration files
- One config file (.csv) describes the input data (e.g. reference files, samples)
- Optional config.yaml file which contains technical details, e.g. Java hepa size and garbage colection, bwa threads, intervals and pairHMM threads for HaplotypeCaller

### Results
- Validated the workflow by the detection of a variant responsile for autosomal recessive dwarfism in the chicken genome, using WGS data from a single affected and 261 non-affected chicken samples.
    - This was a repeat of an original study (Wu *et al*.) in which 11 potential candidate variants were identified (with 1 classified as high impact).
- OVarFlow detected 6 potetial candidate variants (not the same as the 11 candidates detected previously).
- The causative variant identified by Wu *et al*. was among the 6 candidates

#### Optimisation of individual GATK tools
- One problem with JVM is tat its resource utilisation doesn't always scale positivesly with the size of hardware resources
- Heap size and number of garbage collection threads are automatically adjusted to the available hardware.
    - Heap size maxes out at ~25Gb (25% of available memory?)
    - Number of GC threads gorws continuously with the number of given CPU cores.
    - These amounts are usually larger than what is needed by an application to run efficiently

##### Impact of GC thread count
- SortSam, MarkDuplicates, HaplotypeCaller, and GatherVcfs
- Walltime of SortSam, HalotypeCaller, GatherVcfs was not influenced by the number of GC threads
- MarkDuplicates had longer runtime with higher thread counts. 2 threads was optimal.
- Total CPU usage for SortSam, MarkDuplicates increases with GC thread numbers
- Differenced in memory consumption were not as pronounced as with CPU usage.

##### Impact of JVM heap size
- On the same tools
- SortSam benefits from larger heap sizes (12 is optimal).
- Memory footprint is severely affected by the max. allowed heap size for SortSam, MarkDuplcates, and HaplotypeCaller.
- The data for all tools except SortSam were messy and no statistical result could be found

#### Optimisation on the workflow level
- Monitored CPU and memory usage running 6 chicken whole genome fastq files through the workflow.
- Optimising the GC threads reduced initial spikes in memory and CPU usage.
- Optimising heap size also drastically reduced memory utlisation.
- Prior to these optimisations, memory usage maxed at 230-240Gb, and withouth platued at 50Gb.
- Found that running HaplotypeCaller with a single pairHMM thread was preferable to keep each process restricted to a single core, allowing higher parallelisation. This reduced runtime by 5 hours.

### Discussion
- Optimising JVM resources to suit specific hardware architecture is needed for efficient running of GATK workflows.
- Increasing resource sometimes has no effect on walltime but substantial effect on system time, which reduces parallelisation and therefore increases processing time
