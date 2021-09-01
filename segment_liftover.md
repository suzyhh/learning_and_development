# segment_liftover: a Python tool to convert segments between genome assemblies
## Gao, B., Huang, Q., Baudis, M., 2018 (PMC5998006)

### Introduction

- GRCh38 is the newest version of the human genome, and the latest patch still contains >10 million unplaced bases.
- Two general methodologies exist for convertion coordinates between genome assemblies
    1. Re-align the original sequence data (for mapped reads)
        - Highly accurate but time-consuming and computationally demanding
    2. Convert the coordinates using a 'mapping file' (read: chain file)
        - Generally accurate and fast. Some information is likely to be lost.
- Three genome build conversion tools are widely used: liftOver (UCSC), CrossMap (Zhao), Remap (NCBI).

1. UCSC liftOver
    - Web service and command line
    - Comprehensive selection of assemblies, within and between organisms.
2. CrossMap
    - Command line
    - Accepts a wider selection of file types (B/SAM, BigWig, VCF, BED-like, etc...)
    - Results are comparable to liftOver
    - Uses UCSC chain files
3. Remap
    - More limited selection of organisms
    - Conversion based on a different methodology to liftOver and CrossMap
    - 250k row limit
    - Web service and Perl API

- All these tools produce nearly identical results
- Challenges in conversion arise mainly from segments, where the region in the source build does not map to a *continuous* region in the target build. 
- liftOver and CrossMap split the segments into smaller segments and map them to different locations.
- Remap is *integrity-preserving* and preserves the entire segment, mapping the span to the target build.
- Preserving integrity of segments is particularly important for remapping CNVs
    - and also for our use-case, converting intervals in exome bed files
- segment_liftover performs integrity-preseving genomic conversion between genome builds.
- It has two major functional additions to other tools:
    1. Re-conversion by locus approximation when precise conversion of a coordinate failes
    2. Ability to handle any number of files and integration into data processing pipelines, including automatic file traversal, interruption resumption, detailed logging.

### Methods

- Can convert segment and probe files at the same time from a structured directory or list of files.
- UCSC liftOver tool and chain file are used for conversion, followed by approximate conversion on coordinates that failed to convert
- Segment conversion also undergoes additional QC steps to ensure accurate remapping
    - Remapped segment must be on the same chromosome
    - The ratio of the lengths of the original and the remapped segments must be between a range controlled by defined variable 'beta' (default = 2), where 1/beta < ratio < beta
- Approximate conversion will try to find a convertible position in adjacent regions to the un-convertable position. Range and resolution of the search is defined by the *range* and *step_size* parameters.
- Runs in Python. Requires click and pandas (N.B. tested with click==7.1.2 and pandas==1.1.3 as most recent versions of these modules cause segment_liftover to error)

### Use cases
#### Convert arrayMap data from hg19 to hg38

- Converted 44,632 probe file and 44,471 segment files.
- 42 mins to convert 5.5 billion probe positions, 30 mins to convert 4.8 million segments
- Directly converted >99.99% of probes and >99% of segments
    - More unmapped segments as these are more complex and require QC checks
    - Unconverted regions mainy around telomeres, centromeres, and other gene_sparse locations (retrieved from biomaRt using HGNC symbol or ENSEMBL gene ID)
    - From 4.8 million segments, 14,707 were approxiamtely converted, 41,201 were converted but subseqently rejected, and 1,046 were unconvertible.

#### Different conversion strategies

- Using approximate conversion rescues 1 additional segment per file 

[segment_liftover](https://github.com/baudisgroup/segment-liftover)
