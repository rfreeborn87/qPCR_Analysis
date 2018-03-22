#In this script, I simply want to read text file from the ABI7500 and re-write it as a new file.
f = open("E:/OneDrive/Research/Rockwell_Lab/Python/112816_Influenza_Diet_Secondary_Exposure_IFNg_IL2_RF_data.txt","r")
#print((f.read())
#f.close()

new_file = open("E:/OneDrive/Research/Rockwell_Lab/Python/rewritten_data.txt","w")
new_file.write(str(f.read()))
new_file.close()
f.close()