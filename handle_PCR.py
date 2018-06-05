import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

#Read excel file into a pandas DataFrame
original_df = pd.read_excel("E:/OneDrive/Research/Rockwell_Lab/Python/qPCR_Analysis/051218_Influenza_Diet_Primary_M1_IFNg_RPL13a_RF.xls", sheet_name = 'Results', header = None, index_col = 1)
#This sets up a pandas DataFrame such that the columns are what we want (Sample, Target Name, CT, Tm, etc.) and the indices are the wells.
useful_df = original_df.loc['A1':'H12']
useful_df.columns = original_df.loc['Well Position',0:]
useful_df.index.name = 'Well Position'
cols_to_keep = ['Well Position', 'Sample Name', 'Target Name', 'CT', 'Tm1', 'Tm2', 'Tm3']
#Delete columns that don't contain useful data.
for column in useful_df.columns:
    if column in cols_to_keep:
        continue
    del useful_df[column]



#if input('Do you have a No-reverse-transcription control and no-template control?  (y/n)  ') == "y":
#    NRT = input('Please enter the name of your no-reverse-transcription control as it appears in the file:  ')
#    NTC = input('Please enter the name of your no-template control as it appears in the file:  ')
#    useful_df = useful_df[(useful_df[['Sample Name']] != NRT) & (useful_df[['Sample Name']] != NTC)]
#Remove undetermined values and replace with NaN for computations.
useful_df = useful_df.replace('Undetermined', np.nan)


#Make a list of the genes in the dataframe.
list_of_genes = []
for gene in useful_df['Target Name'].unique():
    list_of_genes.append(gene)

#Make a list of dictionaries.  Each dictionary contains the sample name and CT values for a specific gene.
#for_computation holds the Sample : CT for each gene.  Each gene has a dictionary with the sample as keys and CT values as values.
for_computation = []
for item in list_of_genes:
    for_computations = {}
    for row in useful_df.index:
        if str(useful_df.loc[row,'Target Name']) == str(item):
            key = useful_df.loc[row,'Sample Name']
            value = useful_df.loc[row,'CT']
            if key not in for_computations:
                for_computations[key] = value
    for_computation.append(for_computations)

#Define the housekeeper gene.
housekeeper = input('What is your housekeeper gene? Please type it exactly as it appears in your file.  \n')
for index, value in enumerate(list_of_genes):
    if value == housekeeper:
        housekeeper_index = index



#for_computation[index].keys() contains the sample IDs.
#for_computation[index][key] gives the CT value for a gene(index) and sample (key)
#for_computation[housekeeper_index].get(key, 0) gives the RPL13a CT values
#Calculate dCTs and add them to a new list.  dCTs will be stored in dictionaries (each dictionary holds the samples and dCTs for a specific gene).
dCT = []
organized_samples = []
organized_genes = []
for index, target in enumerate(for_computation):
    #print(index,target)
    dCT.append({key: for_computation[index][key] - for_computation[housekeeper_index][key] for key in for_computation[index].keys()})
    organized_samples.append(for_computation[index].keys())
    for key in for_computation[index].keys():
        organized_genes.append(list_of_genes[index])
#print(organized_genes)
dCT_col = []
sample_col = []
for index, value in enumerate(dCT):
    dCT_col.append(list(dCT[index].values()))
    sample_col.append(list(organized_samples[index]))
dCT_col = sum(dCT_col, [])
sample_col = sum(sample_col, [])

useful_df['Organized Samples'] = sample_col
useful_df['Organized Genes'] = organized_genes
useful_df['dCT'] = dCT_col
#Write the reorganized dataframe to a new file for visual confirmation of accuracy.
test_file = 'E:/OneDrive/Research/Rockwell_Lab/Python/qPCR_Analysis/dfs_to_file.xlsx'
writer = pd.ExcelWriter(test_file)
useful_df.to_excel(writer, 'Useful')
writer.save()


control_identifier = input('How can I identify your control values to average?  For instance, if you want your data normalized to wild-type vehicle samples, and you labeled those as WT VEH #, enter WT VEH:  ')
control_dCTs = {}
control_dCT_list = []
control_vals = []
"""for index, val in enumerate(dCT):
    for key, value in dCT[index].items():
        gene = list_of_genes[index]
        if (control_identifier in key) & (useful_df['Target Name'] == gene):
            control_vals.append(value)
    control_dCTs[gene] = control_vals
control_dCT_list.append(control_dCTs)
print(control_dCT_list)"""



#print(list_of_genes)
#print(for_computation)
#for row in useful_df.index:


#print(original_df.head())
#print(useful_df.tail())

#useful_df.to_excel("E:/OneDrive/Research/Rockwell_Lab/Python/AMIRIGHT.xlsx")