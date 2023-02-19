# Python Program to analyse and score proteins
import math
import pandas as pd
import numpy as np

#Replace "SAMPLE.align" with the name of align file generated from DeepMSA
filename = "SAMPLE.align"
f = open(filename, "r")
lines = [[*line] for line in f.read().splitlines()]
no_of_lines = len(lines)
lines_df = pd.DataFrame(lines, dtype="object")
no_of_columns = len(lines_df.columns)
amino_acid = ['A','C','D','E','F','G','H','I','K','L','M','N','P','R','Q','S','T','V','W','Y',' ']
analysis_df = pd.DataFrame(0, index=amino_acid,columns=np.arange(no_of_columns))
for column in lines_df:
    counted_values = lines_df[column].value_counts().to_dict()
    analysis_df[column] = analysis_df.index.map(counted_values)
analysis_df.fillna(0, inplace=True)
pssm_df = analysis_df.applymap(lambda x: x/no_of_lines if x != 0 else 0)
scoring_df = analysis_df.applymap(lambda x: (x + 1)/(no_of_lines+(22*1)) if x != 0 else 0)
log_df = scoring_df.applymap(lambda x: math.log((x)/(1/22)) if x != 0 else 0)
scoring_df.loc["Total"] = scoring_df.sum(axis=0)
pssm_df.to_excel(filename+'_psfm.xlsx')
log_df.to_excel(filename+'_pssm.xlsx')
f.close()


