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
