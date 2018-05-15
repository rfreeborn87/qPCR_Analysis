import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Read excel file into a pandas DataFrame
original_df = pd.read_excel("E:/OneDrive/Research/Rockwell_Lab/Python/092017_Influenza_Diet_Secondary_IFNg_Blimp-1_RF.xls", header = None, index_col = 0)
#This sets up a pandas DataFrame such that the columns are what we want (Sample, Target Name, CT, Tm, etc.) and the indices are the wells.
useful_df = original_df.loc['A1':'H12']
useful_df.columns = original_df.loc['Well',0:]
useful_df.index.name = 'Well'

#print(useful_df.head())


#if input('Do you have a No-reverse-transcription control and no-template control?  (y/n)  ') == "y":
#    NRT = input('Please enter the name of your no-reverse-transcription control as it appears in the file:  ')
#    NTC = input('Please enter the name of your no-template control as it appears in the file:  ')
#    useful_df = useful_df[(useful_df[['Sample Name']] != NRT) & (useful_df[['Sample Name']] != NTC)]

useful_df = useful_df.replace('Undetermined', np.nan)

list_of_genes = []
for_computation = []
for gene in useful_df['Target Name'].unique():
    #print(gene)
    #gene = {}
    list_of_genes.append(gene)

#Make a list of dictionaries.  Each dictionary contains the sample name and CT values for a specific gene.
for item in list_of_genes:
    #print(item)
    for_computations = {}
    for row in useful_df.index:
        #print('I\'m in the for loop')
        if str(useful_df.loc[row,'Target Name']) == str(item):
            #print('It happened!')
            key = useful_df.loc[row,'Sample Name']
            value = useful_df.loc[row,'Cт']
            if key not in for_computations:
                for_computations[key] = value
    for_computation.append(for_computations)
#print(for_computation)
housekeeper = input('What is your housekeeper gene? Please type it exactly as it appears in your file.  ')
for index, value in enumerate(list_of_genes):
    if value == housekeeper:
        housekeeper_index = index

dCT = []
#print(housekeeper_index)
#print(for_computation[0])
for index, target in enumerate(for_computation):
    #print(index, target)
    dCT.append({key: for_computation[index][key] - for_computation[housekeeper_index].get(key, 0) for key in for_computation[index].keys()})
#print(dCT)
listicle = []
for index, value in enumerate(dCT):
    listicle.append(list(dCT[index].values()))
listicle = sum(listicle, [])
print(listicle)
#useful_df['dCT'] = listicle

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