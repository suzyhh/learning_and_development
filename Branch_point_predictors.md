# Assessment of branch point prediction tools to predict physiological branch points and their alteration by variants
## Leman *et al*. (2020) https://doi.org/10.1186/s12864-020-6484-5

### Background
- Approx. 95% of human genes are diversified by alternative splicing
- RNA splicing requires a set of splicing signals, inluding:
    - The donor site (5' ss): defines the exon/intron junction a te 5' end of each intron. Higly conserved. Typically GT.
    - The acceptor site (3' ss): defines theh intron/exon junction at the 3' end of each intron. Higly conserved. Typically AG, preceded by a polypyrimidine tract.
    - The branch point (BP) site: short motif upstream of the poly-p tract. 92% of human BPs contain a highyl conserved Adenosine.
- During the first step in splicing, the BP adenosine attacks the first intronic nt of the upstream 5' ss, forming a lariat intermediate.
- The 5' exone ten attacks te downstream 3' ss, releasing the lariant formed from the intron, and joining the two exons together.
- Splice sites are well characterised and can be reliably predicted in silico
- Branch sites are short and degenerate. They are poorly known and hard to predict.
    - The only highly conserved bases in the BP are T and A, C**T**R**A**Y
    - 95% of BPs are located between 18 and 44 ng upstream of the 3' ss, but can be located up to 400 nt upstream
    - Identification of 'relevant' BPs (i.e., those actually used by the spliceosome) is extremely challenging
- There is a massive limitation in terms of access to experimentally-proven BPs. However, a trio of RNA-se studies in the last decade have broadened this dataset, and as a result several in silico BP predictors have since emerged.
    - Although the dataset is still considered to be far from comprehensive
- Human Splicing Finder (HSF), SVM-BPfinder, Branchpointer, LaBranchoR, RNA Branch Point Selection (RNABPS)

1. HSF
    - Uses a position-weighted matrix with a 7-mer motif as reference (5nt upstream and 1nt downstream of the branch point A)
    - Trained on conserved sequences from ensembl transctips
2. SVM-BPfinder
    - Considers the branch point motif as well as,
    - Conservation of the 3' ss, and,
    - The AG exclusion zone algorithm (AGEZ)
    - Trained on conserved sequences from 7 mammalian species (inc. humans)
3. BPP
    - Combines the BP, 3' ss, and AGEZ algorithm using a mixture model (a popular motif inference method)
    - Trained on conserved sequences from human introns
4. Branchpointer
    - Uses machine learning, trained from a set of experimentally proven BPs
    - Traines on high-confidence BPs
5. LaBranchoR
    - Based on a deep-learning approach
    - Trained on the Branchpointer dataset
    - Implemented a long short-term memory network
6. RNABPS
    - Also based on deep-learning
    - Trained on the Branchpointer dataset
    - Similar to LaBranchoR, uses the LSTM model

- Study benchmarked these 6 tools on their capacity to detect a relevant BP signal and to predict a variant-induced BP alteration
    - Detecting relevant signals highlights the specificity of each tool (can they identify BPs among background noise?)
- Used three sets of data
    - A large set of 3' ss described in the Ensembl database
    - A series of aalternative 3' ss observed in RNA-seq experiments
    - A collection of human variants within the BP area (-18 to -44) and their in vitro RNA studies: to assess the prediction of variant effect on BP function

### Results
#### Detection of BBPs among the physiological and alternative splice acceptor sites
- Retrieved 264787 Ensembl 3' ss and added >1.1M random AGs, used as control data.
- Performed ROC curve analysis on:
    - SVM-BPFinder, BPP, LaBranchoR, and RNABPS
- Branchpointer was the highest performer, with an acuracy of 99.49% and a positive predictive value of 30%
