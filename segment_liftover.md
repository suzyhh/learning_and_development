# segment_liftover: a Python tool to convert segments between genome assemblies
## Gao, B., Huang, Q., Baudis, M., 2018 (PMC5998006)

### Introduction

- GRCh38 is the newest version of the human genome, and the latest patch still contains >10 million unplaced bases.
- Two general methodologies exist for convertion coordinates between genome assemblies
    1. Re-align the original sequence data (for mapped reads)
        - Highly accurate but time-consuming and computationally demanding
    2. Convert the coordinates using a 'mapping file' (read: chain file)
        - Generally accurate and fast. Some information is likely to be lost.

