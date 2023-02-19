import pandas as pd
#import numpy as np

#reading the fasta file
#Replace 'Sample.fasta' with the name of fasta file
f=open('Sample.fasta','r')
lines=f.readlines()
seq = lines[1]

# read Physicochemical properities
pp = pd.read_excel('PP.xlsx')
AminoacidsSeq = pp['letter ']
#initialise the feature3 array with zeros
Phy_prop = pd.DataFrame(columns=pp.columns)

for s in range(len(seq)-1):
    for a in range(len(AminoacidsSeq)):
        if seq[s] == AminoacidsSeq[a]:
            #print(seq[s],AminoacidsSeq[a])
            Phy_prop.loc[s] = pp.loc[a]

# # #Replace 'Sample_pp.xlsx' with the name of excel to which to store the result
Phy_prop.to_excel('Sample_pp.xlsx')

















