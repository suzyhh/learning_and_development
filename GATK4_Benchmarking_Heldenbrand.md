# Recommendations for performance optimizations when using GATK3.8 and GATK4
## Heldenbrand, et al. (2019), https://doi.org/10.1186/s12859-019-3169-7

### Background
- GATK is a popular variant calling toolkit
- WES/WGS is now embedded into clinical practice and has many applications. We now have an increased need for faster and more efficient variant calling pipeline, particularly as our ability to actualy *sequence* DNA is becoming increasingly cheap and fast.
- GATK workflows can take many hours or days
- Many proprietary solutions have popped up in recent years (e.g. Dragen), but these are for-profit, closed-source programmes inaccessible to many
- In response, the Broad Institute partnered with Intel to optimise computational performance and released GATK4.
    - GATK3.8 was the final release of the "traditional" Java-based GATK
- GATK4 was designed with the vision of eventually implementing the tools in Spark (a MapReduce platform), although most are either not developed in Spark or in Beta production.
- Non-Spark GATK tools have also been rewritten from GATK3.8 in order to improve speed
- This project looked to benchmark non-Spark GATK4 tools against GATK3 tools.

### Methods
- GATK3.8 vs. GATK4.0.12
- USed the GATK Best Practices from duplicate marking -> variant calling.
- INDEL realignment was not tested as it has been removed in GATK4
- The dataset used was the WGS NA12878 (20x coverage), aligned with BWA MEM against the hg38 reference

### Results
#### GATK3.8 tool-level thread scalability
- Data-level parallelisation
- In GATK3.8, controlled by the -nct and -nt options (how many cores, and how many threads/core)
- Walltime was measured for each tool invoked with a range of thread counts (range: 1-40)
- Maintained -nt 1 and modified nct
- Tested tools responded uniquely to multi-threading and all had suboptimal scalability (walltime decreasd lss than the thread increase factor)
- Improvements seen at lwoer thread counts plateau as thread count is increased further.
    - Performance of PrintReads actually degrades about 3 threads
- The suboptimal scalability can be attributed to a number of factors:
    - Tasks are often I/O-heavy, and latency in disk acces and the network can degrade performance
    - Using SSDs can help combat this

#### GATK4 parallel garbage collection
- Java mecanism to automatically remove variable and objects from memory that are no longer needed.
- Tested different number of PGC threads given to each tool
- Enabling PGC had no impact on the performance of ApplyBQSR or HaplotypeCaller
- MarkDuplicates had optimal performance at 2-4 threads
- BaseRecalibrator responded in an unpredictable way to different thread counts.
- Didn't find any significant improvements in GATK3.8 with increasing threads.
- GATK3.7 has previously been reported to respond positively to PGC scalability.
- Recommend users run a cursory PGC thead scalability analysis on their own system as there is likely to be architecture-specific results.

#### Asyncronous I/O in GATK4
- GATK4 uses Samtools I/O and Tribble I/O for async read/write.
    - Tribble is specialised and used mainly for index files
- Had the best results from enabling async I/O for Samtool and disable it for Tribble

#### PairHMM scalability in GATK4 HaplotypeCaller
- Intel and the Broad Institute created the Genomics Kernal Library (GKL), which introduced AVX optimised versions of the PairHMM and Smith-Waterman algorithms.
- The PairHmm algorithm also benefits form multi-threading.
- Ran a sweep of 1-40 pairHmm threads
    - 10 threads was optimal for HaplotypeCaller performance

#### Splitting by chromosome
- Process-level parallelisation: process each interval in parallel
- Tested for "within-node" and "between-node" splitting
- The number of threads given to the tools was reduced accordingly as the number of interval was increased

1. GATK3.8 Results
    - The benefit of splitting beyond 3 chunks is negated by the performance degradation due to a reduced thread count
    - Between-node (no limit on thread count) splitting saw decrease in walltime up to 12 chunks (the highest tested), although the most gains are to be had at 6 chunks

2. GATK4 Results
    - Split within-node (decreasing the number of given pairHmm threads accordingly), walltime continues to decrease up to 16 chunks (the most tested)
    - Were the other tools also split using -L?

#### Throughput
- Scattering multiple samples running GATK4
- Walltime increases as you increase number of samples processed in parallel
- Overall throughput increases up to ~20 samples/node (total of 40 cores)

### Discussion
- When applied together, the optimisations reduce walltime:
    - GATK3.8 from 21.7 hours to 15.3 hours (29% improvement)
    - GATK4 from 24.9 hours to 20.7 hours (17% improvement)
- Also splitting by chromosome further improves walltime:
    - GATK3.8 reduced to 5 hours when the BAM is split into 16 chunks (77% imprv)
    - GATK4 reduced to 3.4 hours when split into 12 chunks (84% imprv)
- Financially, there is a trade-off between speed and cost.
    - For time-critical analysis, the recommendation is to use GATK3.8, splitting into 12 chunks, the total walltime is 3.6 hours, costing $41 per sample.
    - For high-throughput analysis, the recommendation is to use GATK4, if you run 40 samples on one node, the total walltime is 34 hours, costing $2.60 per sample.
