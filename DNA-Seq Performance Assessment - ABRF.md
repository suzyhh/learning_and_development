# Performance assessment of DNA sequencing platforms in the ABRF Next-Generation Sequencing Study
## Foox et al. (2021), 10.1038/s41587-021-01049-5

### Background
- The ABRF (Association of Biomolecular Resource facilities) is an American association "dedicated to advancing core and research biotechnology laboratories through reserch, communication, and education"
- Has several established research groups (e.g. ABRF Next Generation Sequencing Group, Technology Research Group, Metagenomics Research Group, etc...)

- The aim of this stufy was to benchmark current genomics technologies and provide a resource for informing experimental design and NGS variant calling:
    - Paired end Illumina technology (HiSeq, NovaSeq)
    - Ion S5 and Proton
    - PacBio circular consensus sequencing (CCS)
    - Oxford Nanopore (PromethION, MinION, Flongle)
    - BGISEQ-500, MGISEQ-2000
    - GenapSys GS111

### Main
- Due to the increasing afforability and accessibility of genomic sequencing, there is now greater diversification of sequencing techniques and methodologies - both wet lab and computational.
- This has led to the development of clinical standards and validation/benchmarking standards.
- Unlike previous technologies, such as for microarrays, there is not yet a high-quality and large-scale study looking into the reproducibility and QC of DNA-seq across all key platforms.
- The GIAB Consortium facilitated genomics benchmarking with their reference materials, benchmarking tools, sequence data, and variant reference sets.

#### Brief Methods
- This ABRF NGS DNA-seq study uses the following reference materials:
    - The "Ashkenazi trio" (NIST RM 8392), consisting of proband (male, HG002), mother (HG004) and father (HG003). Consented through the Personal Genome Project (PGP).
- Inter- and intra-laboratory DNA-seq replicates of the Ashkenazi trio are analysed
- Genomic (TruSeq PCR-free whole-genome libraries) and Exomic (AmpliSeq exome libraries)
- Also analysed are: 
    - Three individual bacterial strains
    - A metagenomic mixture of ten bacterial species to study the effects of GC content and library complexity
- Replicates were generated across:
    - 5 Illumina platforms
    - 3 ThermoFisher Ion Torrent platforms
    - BGISEQ-500, MGISEQ-2000
    - GenapSys GS111
    - ONT platforms, Flongle, MinION, PromethION
    - Using publically available PacBio data for the proband (HG002)
- Data were tested within the most challenging genomic regions, represetned by the UCSC RepeatMaske regions to highlight differences between each instrument
- Data generated were examined for performance and reproducibility over a range of base compositions and GC content profiles.

### Results
#### Data quality
- Sequencing depth varied across experiment type
    - Ultradeep genomic coverage of bacterial taxa (nearly 1000x mean coverage)
    - Shallow human genomic coverage (<1x mean coverage)
    - Most WGS libraroes had between 25x and 80x mean coverage.
- A coverage threshold for downstream analyses was set at 25x.
- Overall sequence quality was consistently high across all libraries.
- Human data were aligned against GRCg38 with decoy contigs (containing EBV sequence and human genomic seqs that could not be placed on chromosomes in the reference), these deflected: 
    - 1% of Illumina and GenapSys reads
    - 0.5% BGISEQ and MGISEQ reads
    - 2-5% of long-read data
    - Nearly no ThermoFisher (Ion) reads

- Mapping rates were consistent within instruments, and highly variable between them
- BGISEQ and GenapSys had the lowest unique mapping rates of short-read sequencers, and highest multi-mapping rates
    - Maybe due to relatively short read lengths (2x100bp and 150bp single end, respectively).
- ThermoFisher has slightly better mappign rates than Illumina and MGI platforms - becasue of fewer hard to map exonic regions
- Long read: PacBio had more accurate mapping than ONT platforms
- The PromethION had lower mappubg rates, ~85% as there was a substantial fraction of short reads that did not map
- Short read: BGI and MGI has lower duplicate and unmapped read rates than Illumina. BGI had lower properly mapped rate.

- All replicates had highly consistent capture per GC bin, showing no platofmr-specifci effect.
    - WGS and WES revelead differences in GC composition
- The AmpliSeq exome panel used on the Ion Torrent instruments showed highly consistent on-target mapping.

- For bacterial species, mappability was found to be directly related to the species sequenced. There was high variablity between species, but results were highly consistent within each instrument.

#### Normalised coverage analysis
- Only used replicates with sufficient coverage ( mean depath <10x, MAPQ > 20). alignments were normalised to a global mean of 25x ccoverage per replicate.
- Coverage distributiosn were highyl consistent among the platforms - inluding short and long reads.
- Within "challening" genomic regions (Alu elements, repeats of various forms and complexities) however, platform-specific trends could be seen.
    - The HiSeq 2500 and BGI platforms under-performed in most categorised difficult regions.
    - However, the HiSeq 4000 and X10 performed well in most regions, although the NovaSeq (2x250bp) performed better across the board.
    - In the end though, long-reads tech (PacBim PromethION) outperformed all other platforms.

#### Sequencing mismatch rate
- Rates of mismatches among reads aligned to the reference genome in UCSC RepeatMasker regions.
- Short-read platforms had lower mismatch rates across the board compared to ONT
- PacBio reads had mismatch rates equal to or less than the short reads in all regions except satellite regions.
- Among short-read platfoorms, the BGISEQ-500 came out on top, then HiSeq platforms, with the MGISEQ-2000 coming last. 
- NovaSeq 2x250bp had a greater mismatch rate than the 2x150bp chemistry.
- Higher rate of mismatch observed at GC% extremes for all platforms
- All short reads platofrms and the PacBio showed increased error rates towards the 3' end (common knowledge for me in short-read sequencing), whereas ONT reads had flat (high) rates across the read length.

- When repeats are stratified using the Tandem Repeat Finder into:
    - True homopolymers (stretches of poly-N in the reference)
    - Short tandem repeats (STRs), ordered by entropy (repeat complexity).
- For both of these, PacBio showed the lowest rate of mismatch
- ONT platforms has flat and high mismatch rates.
- Short-reads tech has rougly the same performance in homopolymer regions >25bp.
- All (inc. PacBio) platforms performed worse in longer homopolymer regions or in areas fo low entropy.

- Observations from Figure 3:
    - As expected from prior knowledge/impressions, ONT has the highest mismatch rate, and PacBio the lowest.
    - I haven't encountered GenapSys before, but it also has higher mismatch rates than short-reads tech, not not quite as high as ONT
    - Read length matters w.r.t mismatch rate for the NovaSeq
    - The three HiSeq platofrms are comparable
    - The GenapSys platform has comparable mismatch rate in the homopolymer repeats, but a higher rate for STRs - here it shows the same "pattern" as ONT platforms, but with lower mismatch rates
    - In higher entropy STRs (more complex repeats, >1.75-ish), short-read tech actually has a lower mismatch rate than the PacBio

#### SNV and INDEL detection
- Mismatches were identified as varants against GrCh38 using the GIAB high-confidence variant truth set, using:
    - Every genome replicate of the proband (HG002) with a minimum depth >10x
    - RTG vcfeval

- Compared several variant callers
    - DeepVariant
    - GATK HaplotypeCaller
    - Sentieon Haplotyper
    - Strelka2
    - Clair2 (long reads)
- BGI, MGI, and NovaSeq 2x250bp had the highest precision and recall rates
- HiSeq 500 and 4000 had the worst performance
- PacBio (Clair2) had highly-comparable performance to short-read variant detection. ONT performance was the lowest of all platforms.
- Generally, DeepVariant had the highest accuracy rates of the variant callers.
- Strelka2 was as precise as DeepVariant, but not as sensitive.
- GATK and Sentieon callers were the least precise. Sentieon was slightly less sensitive than GATK
- All subsequent analyses were carried out using DeepVariant.

- Variants were again stratified using UCSC RepeatMasker.
    - Globally, sequencing platofmrs showed similar perforamance
    - L1, L2 repeats, and LTRs had the most accurate calls across platforms
    - Low-complexity regions and simple repeats were the least accurate
    - Satelitte and Alu elements in the middle

- In SNV regions
    - HiSeq 2500 and ONT platforms captured the fewest TP SNVs.
    - NovaSeq and MGI platforms captured the greatest number of TP CNVs
- For INDELs
    - ONT failed to capture the majority of TP INDELs, followed by the PacBio, and then the HiSeq platforms.
    - NovaSeq and MGI platforms again performed the best

- In clinically-relevant regions (using CLINVAR and OMIM), the NovaSeq chemistries achieved teh greatest accuracy. PacBio had the greatest precision.
- OMIM genes were harder to detect variants from than CLINVAR genes
- Across the exome (to inlude ThermoFisher exome samples), short-read (NovaSeq, BGI, MGI) showed the greatest sensitivity and precision, followed by HiSeq, then PacBio.

- Observations from Figure 4:
    - The precision and sensitivity for HiSeq 2500 and 4000 replicates were not tightly clustered, and also showed greater variability between variant callers.
    - GATK precision for the HiSeq 4000 replicates had a high spread and was generally lower than other callers.
    - Detection of INDELs follows a normal distrubiton across size (-50bp to +50bp). Highest detection for 1bp INDELs

#### Structural variant detection
- A high-quality reference SV set was constructred using 3x ONY and 3x PacBio datasets using high-concordance SV calls: the "HG002 Reference SV set"
- Identified an average of 22,000 SVs per sample. ONT platforms detected *slightly* (~2.5%) more SVs compared to PacBio.
- Short-read HG002 samples sequenced on HiSeq platforms (the only included due to technical limitations) had 12,435 SVs detected. 95% of these overlapped with GIAB high-confidence regions
- HiSeq platforms struggled the most with detecting insertions.
- The most variability in HiSeq SV data originated from which SV caller was used for SV detection. then teh sequencing intrumant, and then replicate-level variability.
- False negatives were observered primariliy, rather than false positives (they expected to see mostly false positives)

#### Bacterial genome sequencing
- To measure performance on genomes with high and low GC content
- Taxonomic composition of the metagenomic pool was found to be quite variable both within and between sequencing platforms.
- Replicates within platforms were highly similar except for two Ion Torrent outliers.
- Flongle and MinION results clustered closely to each other and to the HiSeq.
- The S5 was the most dissimilar of all platforms.
- Taxonomic composition was impacted by the GC% of each taxon
    - low-GC and gram-positive, and high-GC taxa were underrepresented.

### Discussion
- Long-read technologies are better suited to provide coverage in difficult to sequence genomic regions
- However, some short-read platforms (HiSeq X10 and 4000) perform as well as the tested long-read platforms in most regions
- Telomeric and centromeric regions are the most challenging, and along with a subset of satellites, were poorly covered across all platforms tested.

- The mismatch rate in GC-extreme regions and towards teh 3' end of reads was increased in all platforms. The PacBio provided the highest nt accuracy in all contexts.
- Although greatly improved in recent years, ONT platforms still have lower accuracy than all other platforms in all genomic regions.

- Only a single replicate was available for several platforms, and this limited some of the downstream analyses. Intraplatform repdocability for these platforms could therefore not be tested and should be looked at in future.

- Of tested variant callers, DeepVariant had the highest sensitivity and specificity against the GIAB truth set.
    - A deep-learning call that is trained specifically on single-ethnicity, B lymphocyte-derived cell line genomes. The risk is overfitting to training samples, resulting in unpredictable performance in other use cases
- Sentieon Haplotyper had the poorest performance, but is considerably faster.
- Detection of TP SVs was most heavily influenced by the variant caller used, *not* the seqencing platform

- Error rates were consistent across platforms and laboratories.
- Emerging platforms from BGI, GenapSys and ONT had comparable performance to established platforms, showing that the genomic landscape is still able to diversify and change
