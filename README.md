# Protein Secondary Structure Predictor using Residual Dense Network

## Introduction

Proteins are chains of amino acids joined together by peptide bonds. Many conformations of this chains are possible due to the many possible combinations of amino acids and rotation of the chain in multiple positions along the chain. It is these conformation changes that are responsible for differences in the three dimensional structure of proteins.

protein-molecule-structure

Protein structure prediction is one of the most important goals pursued by bioinformatics and theoretical chemistry; it is highly important in medicine (for example, in drug design) and biotechnology (for example, in the design of novel enzymes). [1]

When we talk about the structure of proteins, four different structure levels are mentioned: the primary, secondary, tertiary and quaternary structure.

![image](https://user-images.githubusercontent.com/62247880/219960074-375d5980-3f2d-4c49-8a1d-cf05c40d0776.png)

Protein structure prediction is one of the most important goals pursued by bioinformatics and theoretical chemistry; it is highly important in medicine (for example, in drug design) and biotechnology (for example, in the design of novel enzymes). [1]

When we talk about the structure of proteins, four different structure levels are mentioned: the primary, secondary, tertiary and quaternary structure.

![image](https://user-images.githubusercontent.com/62247880/219960121-bed13c5b-a2ce-4a0d-ad12-e0e9e1807497.png)

Protein primary structure is the linear sequence of amino acids in a peptide or protein.

Protein secondary structure is the three dimensional form of local segments of proteins. Secondary structure elements typically spontaneously form as an intermediate before the protein folds into its three dimensional tertiary structure. Both protein and nucleic acid secondary structures can be used to aid in multiple sequence alignment.

The tertiary structure is however particularly interesting as it describes the 3D structure of the protein molecule, which reveals very important functional and chemical properties, such as which chemical bindings the protein can take part in.

Predicting protein tertiary structure from only its amino acid sequence is a very challenging problem, but using the simpler secondary structure definitions is becomes more tractable. [2]

I focused on the primary and secondary structure (SS), more specifically on using Convolutional Neural Networks (CNNs) for predicting the secondary structure of proteins given their primary structure.

## Protein Structures and Protein Data

The primary structure of proteins are described by the sequence of amino acids on their polypeptide chain.

![image](https://user-images.githubusercontent.com/62247880/219960172-559a3446-0021-45d0-8c12-50242cbdc15e.png)

There are 20 natural occurring amino acids in the human body which, in a one letter notation, are denoted by: ’A’, ’C’, ’D’, ’E’, ’F’, ’G’, ’H’, ’I’, ’K’, ’L’, ’M’, ’N’, ’P’, ’Q’, ’R’, ’S’, ’T’, ’V’, ’W’, ’Y’. ’A’ standing for Alanine, ’C’ for Cysteine, ’D’ for Aspartic Acid etc. A 21st letter, ’X’, is sometimes used for denoting an unknown or any amino acid.

Instead of using the primary structure as a simple indicator for the presence of one of the amino acids, a more powerful primary structure representation has been used: Protein Profiles. These are used to take into account evolutionary neighborhoods and are used to model protein families and domains. They are built by converting multiple sequence alignments into position-specific scoring systems (PSSMs). Amino acids at each position in the alignment are scored according to the frequency with which they occur at that position. [2]

![image](https://user-images.githubusercontent.com/62247880/219960210-5984bade-3cf2-400e-ba54-8623bf8bb4ba.png)

A protein’s polypeptide chain typically consist of around 200-300 amino acids, but it can consist of far less or far more. The amino acids can occure at any position in a chain, meaning that even for a chain consisting of 4 amino acids, there are 204 possible distinct combinations. In the used dataset the average protein chain consists of 208 amino acids.

Proteins’ secondary structure determines structural states of local segments of amino acid residues in the protein. The alpha-helix state for instance forms a coiled up shape and the beta-strand forms a zig-zag like shape etc. The secondary structure of the protein is interesting because it, as mentioned in the introduction, reveals important chemical properties of the protein and because it can be used for further predicting it’s tertiary structure. When predicting protein's secondary structure we distinguish between 3-state SS prediction and 8-state SS prediction.

For 3-state prediction the goal is to classify each amino acid into either:

alpha-helix, which is a regular state denoted by an ’H’.
beta-strand, which is a regular state denoted by an ’E’.
coil region, which is an irregular state denoted by a ’C’.
The letters which denotes the above secondary structures are not to be confused with those which denotes the amino acids.

For 8-state prediction, Alpha-helix is further sub-divided into three states: alpha-helix (’H’), 310 helix (’G’) and pi-helix (’I’). Beta-strand is sub-divided into: beta-strand (’E’) and beta-bride (’B’) and coil region is sub-divided into: high curvature loop (’S’), beta-turn (’T’) and irregular (’L’). [2]

E = extended strand, participates in β ladder
B = residue in isolated β-bridge
H = α-helix
G = 3-helix (3-10 helix)
I = 5-helix (π-helix)
T = hydrogen bonded turn
S = bend
_ = loop (any other type)

For the scope of this project the more challenging 8-state prediction problem has been chosen.

## Dataset

A five datasets of protein sequences are chosen from Protein Data Bank (PDB) for training, validating and testing. 
The first dataset consists of 11,897 X-Ray structure protein sequences [3] selected from Protein Data Bank (PDB). The following criteria are satisfied by each selected protein sequence: (a) Its sequence similarity should be less than 25%. (b) It must have a minimum resolution of 2.5 A◦. (c) It should belong to the X-ray experimental method only. 
The second dataset consists of  621 NMR structure [4] protein sequences. There is a more significant difference between X-ray and NMR structures of the same protein than between various X-ray structures found for the protein and even more than the differences between different NMR structures of the protein. All the proteins are selected from PDB based on the main condition that they should only belong to the NMR structure.
The third dataset consists of 6729 protein sequences selected randomly from the PDB. Each of these chosen protein sequences satisfies the following conditions: (a) Any two selected protein sequences should not have more than 25% similarity between them. (b) The length of the selected protein sequence should lie between 26 and 700. (c) It should have a unique protein chain. (d) All the chosen protein sequences should be deposited into the database prior to the CASP13 experiment.
The fourth dataset consists of  821 protein sequences, including 105 and 96 protein sequences from CASP 11 and CASP 12, respectively, and  621 NMR structure protein sequences. CASP datasets are publicly available and can be obtained from the CASP (https://predictioncenter.org/index.cgi.) website  under the target list for CASP 11 and CASP 12.
The fifth dataset used as test dataset is Critical Assessment of Protein Structure Prediction (CASP) which were the most commonly used dataset for testing the accuracy of the protein secondary structure methods. The CFLM used 122 TBM target protein sequences together from CASP13, and CASP14, respectively. These datasets are publicly available on the CASP website (https://predictioncenter.org/index.cgi.) under the target list for CASP  13 and CASP 14, respectively.
All protein sequences in one dataset are compared with protein sequences of other datasets used in this work and ensure that none of them are repeated. ECOD classification [5,6] s applied to ensure that the CFML produces the result rather than copying it from all its training sets. Table 2 lists the number of proteins in each dataset used in this work.  

## Cascaded  Feature Learning Model (CFLM) for protein secondary structure prediction 

This paper presents Cascaded Feature Learning Model (CFLM) for predicting protein secondary structure, which utilizes transfer learning approach based on a residual dense network (RDN)[6] which consists of 20 RDBs(Residual Dense Blocks). It has two levels of the transfer learning process. Initially, RDN is directly trained using Dataset 1. In the 1st level, the knowledge gained from this learning is transferred into the next level of transfer learning by blocking 11 RDB of RDN. Rest 9 RDB of RDN is re-trained using Dataset 3. The knowledge gained from this level is transferred into the 2nd level of transfer learning by blocking 4 out of the 9 RDB of RDN, and the remaining 5 RDB of RDN are re-trained using Dataset 2. 

## Features

1. Position-Specific Scoring Matrix (PSSM) and Position-Specific Frequency Matrix(PSFM) features obtained using DeepMSA algorithm

"psssm_psfm.py" can be used to find the PSSM and PSFM of the datasets. 
The "SAMPLE.align" is the sample align file we obtained using DeepMSA algorithm. 
The "SAMPLE.align_pssm.xlsx" and "SAMPLE.align_psfm.xlsx"shows the PSSM and PSFM 

2. Solvent accessibility features

"1GZM_1" is the sample of solvent accessibility features obtained from the website

3. Physicochemical properties features

"Physicochemical properties.jpg" shows the Physicochemical properties of all the amino acids
"PP.py" can be used to find physicochemical properties features of a protein sequence from fasta file
"Sample.fasta" is the sample fasta file of protein sequence
"PP.xlsx" is the excel file that contains the Physicochemical properties of all the amino acids
"Sample_pp.xlsx" shows the the Physicochemical properties of a protein sequnce

Training
"





## References

[1]: Ozkan SB, Wu GA, Chodera JD, Dill KA: Protein folding by zipping and assembly. ProcNatlAcadSciU S A 2007, 104(29):11987-11992.

[2]: Geethu, S., and E. R. Vimina. "Three-Dimensional Protein Structure Prediction–Exploratory Review." Advances in Electrical and Computer Technologies: Select Proceedings of ICAECT 2020. Springer Singapore, 2021.

[3]: Maveyraud L, Mourey L (2020) Protein X-ray crystallography and drug discovery. Molecules 25(5):1030

[4]: Morelli, Xavier, et al. "Heteronuclear NMR and soft docking: an experimental approach for a structural model of the cytochrome c 553− Ferredoxin Complex." Biochemistry 39.10 (2000): 2530-2537.

[5]:42.	H. Cheng, R. D. Schaeffer, Y. Liao, L. N. Kinch, J. Pei, S. Shi, B. H. Kim, N. V. Grishin. (2014) ECOD: An evolutionary classification of protein domains. PLoS Comput Biol 10(12): e1003926.

[6]: H. Cheng, Y. Liao, R. D. Schaeffer, N. V. Grishin. (2015) Manual classification strategies in the ECOD database. Proteins 83(7): 1238-1251.


