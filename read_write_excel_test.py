#In this script, I simply want to read an file from the ABI7500 and re-write it as a new file.

#For files with only one sheet_names
import pandas as pd
df = pd.read_excel("E:/OneDrive/Research/Rockwell_Lab/Python/092017_Influenza_Diet_Secondary_IFNg_Blimp-1_RF.xls")
#print(df.head())
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