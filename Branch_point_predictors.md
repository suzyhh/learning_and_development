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
- ROC-AUC analysis
	- ROC is a probability curve
	- AUC represents the degree/measure of separability, i.e. how much the model is capable of distinguishing between classes.
	- The higher the AUC, the better the model is at predicting classes correctly.
	- ROC curves are plotted with the TPR/sensitivity (y-axis) against the FPR (1-specificity, x-axis)

- BPP exhibited the best performance based on AUC analysis (AUC = 0.818), but literally *just*, the other tools were between 0.728 and 0.811
- However, BRancpointed had the highest performances (accuracy = 99.49% and PPV 30.06%)
	- For reference, the PPV for the other 4 tools was 0.42% - 0.7% and the accuracy between 64% - 75%
- Only 0.15% of the 3'SS had a branch point predicted by all 5 tools (out os >75m 3'ss)


- 51,986 alternative 3'ss were identified to assess branchpoint prediction amongst alternative acceptor sites. A similar num. of control 3'ss were added
- Branchpointer again shower the highest accuracy (65.8%), however sensitivity was reduced by >60% to 32%
- They then compared expression of alternative sites (from RNA-Seq data) with and without a BP predicted by the bioinformatics tools
	- Reardless of which tool made the prediction, 3'ss with a predicted BP had significantly higher expression than those without a predicted BP
	- The greatest difference in expression was seen for Brancpointer
	- But BRanchpointer *score* was not correlated with expression amongst sites with a predicted BP

#### *in silico* prediction of the splicing effect of variants in the BP area
- Dataset: a collection of experimentally characterised variants mapping within BP areas that potentially had an effect on splicing (120 variants in 86 introns, in 36 different genes).
	- 62 of these variants were obtained from unpublished data
	- 38/120 (31%) of the variants were found to alter splicing under the authors' experimental conditions
- The 38 spliceogenic variants were found in 30 different introns and had varied effects on splicing:
	- 22 induced exon skipping
	- 10 caused full intron retention
	- 6 activated the use of another cryptic 3'ss, located up to 147nt upstream of the 3'ss and 38nt downstream of the initial acceptor site
- Of these spliceogenic BP area variants, they analysed the distriution of variants according to the position of the predicted BP
	- So where is the variant with respect to the predicted BP?
	- The best common motif was a 4-mer starting 2nt upstream and 1nt downstream of te BP A, corresponding to the motif TRAY
- For the 4-mer motif, BPP had the highest accuracy (89%) and sensitivity (84.21%) and second highest specificity (91.46%) using the n=120 dataset
- Variants affecting splicing were mostly located at the BP A and at -2nt (2nt updtream of the branchpoint A: T)
	- Splicing anomolies were predicted from 10/10 variants at position -2 and for 15/18 variants predicted to be located at the BP A that were predicted by BPP
	- The remaining 3/18 BP A variants were placed outside BP motifs by BRanchpointer and LaBranchoR but were predicted to be the BP A by SVM-BPfinder

- Calculated delta scores for each tool to assess the discriminating capability of each at identifying splicing defects from BP variants
	- This is literally just the difference between two numbers as far as I can tell
	- Sensitivity against 1-specificity

### Discussion
- FRom Ensembl data, Branchpointer had the best performance, ighlighting the utility of machine-leaaarning compared to the support vector machine (SVM-BPfinder) and mixture models (BPP)
- Deep-learning tools (RNABPS and LaBranchoR) had lower accuracy than ML Branchpointer.
	- The authors theoraise this is to do with how the models were trained: Branchpointer used a large collection of negative BPs as control data, so perhaps is more powerful to detect real BPs among background noise (hence the higher PPV). Branchpointer also takes into account the transcript structure and only considers predicting BPs occuring -44 and -18 upstream of te 3'ss
- Branchpointer possibly less good at predicting alternative BPs (low sensitivity) because it was trained on high-confidence BPs, with low-confidence BPs being considered negative
- for identifying spliceogenic variants, the best prediction strategy was to consider te variant as impacting splicing **if it is located in the BP motif**
	- BPP had the highest accuracy
- So only 31% of variants in the **BP area** affected splicing, whereas 82% of variants that are in the **BPP-predicted BP motif** alter splicing
- Potential therefore for using BPP to prioritise variants occurring in this region.
	- Authors determined that the 4-mer **T**R**A**Y in the BP motic was the most impacted by variants. Therefore **a variants in this motif has a high probability to alter splicing** (probabbility of 82% with BPP)
	- The highly conserved di-nucleotides at positions 0 and -2 were critical to BP recognition

### Conclusion
- Branchpointer is best at detecting real BPs amongst background noise
- BPP-predicted BPs were more efficient to predict the impact of variants on BP usage and BPP was able to predict the 5-mer BP motifs (accuracy 89.17%)
- There is an adcantage of studying the BP area (-44-18 intronic positions)
- These tools are usful for variant **prioritisation** for *in vitro* RNA studies

### Extra notes
- BPP has a github, but has not been updated in 5 years and doesn't look active/supported. It also only runs in Pyton2.7. Should we be using an unsupported tool that depends on a defunct version of Python?
