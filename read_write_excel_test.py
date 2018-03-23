#In this script, I simply want to read an file from the ABI7500 and re-write it as a new file.

#For files with only one sheet_names
import pandas as pd
df = pd.read_excel("E:/OneDrive/Research/Rockwell_Lab/Python/092017_Influenza_Diet_Secondary_IFNg_Blimp-1_RF.xls", header = 7)#index_col = 0)
#This will print the name of each column
#print(df.columns[0])
#print(len(df))


#To facilitate working with multiple sheets from the same file, the ExcelFile class can be used to wrap the file and can be passed into read_excel
#xlsx = pd.ExcelFile('path_to_file.xls')
#df = pd.read_excel(xlsx, 'Sheet1')

#To write a new excel file
#df.to_excel('path_to_file.xlsx', sheet_name='Sheet1')
df.to_excel("E:/OneDrive/Research/Rockwell_Lab/Python/092017_Influenza_Diet_Secondary_IFNg_Blimp-1_RF.xlsx",sheet_name="Cool")

"""#In order to write separate DataFrames to separate sheets in a single Excel file, one can pass an ExcelWriter.
with ExcelWriter('path_to_file.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')"""

#For more information, see the pandas tutorial at http://pandas-docs.github.io/pandas-docs-travis/io.html#writing-excel-files
"""
#For filtering excel data:
#This is just making a new dataframe to work with called df2
In [41]: df2 = df.copy()
#This creates column E of the dataframe
In [42]: df2['E'] = ['one', 'one','two','three','four','three']
#This prints the dataframe.
In [43]: df2
Out[43]: 
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three
This filters the dataframe to only print out the values where the conditions are met.  This is what I need to filter gene names and Ct values.
In [44]: df2[df2['E'].isin(['two','four'])]
Out[44]: 
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
"""


#Make the target name the index
df_indexed = df.set_index("Target Name",drop = False)
#Write indexed DataFrame to file.
df_indexed.to_excel("E:/OneDrive/Research/Rockwell_Lab/Python/092017_Influenza_Diet_Secondary_IFNg_Blimp-1_RF_indexed.xlsx",sheet_name="Cool")
#Write only the rows containing RPL13a in the index to file.
df_indexed.loc['RPL13a'].to_excel("E:/OneDrive/Research/Rockwell_Lab/Python/test_excel_file.xlsx",sheet_name = "RPL13a")

#I am going to test filtering to see if I can subtract Ct of target from Ct of RPL13a.
#This goes through each column.
#for i in df_indexed:
    #If the column is the Ct, print out the column.
    #if i == "Cт":
        #Print the whole column.
        #print(df_indexed[i])
listicle = []
n = 0
while n < len(df_indexed):
    listicle.append(df_indexed.iloc[n,df_indexed["Cт"]])
    n += 1

print(listicle)
        