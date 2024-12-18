from PIL import Image
import os
import glob
import json


png_files=glob.glob('C:\\Users\\KIIT\\OneDrive\\Pictures\\*.png')

#create a dictionar out of the list of png files
png_dict={}
x=0
for i in png_files:
    x+=1 
    png_dict[f"{x}"]=os.path.getsize(i)

for i in png_dict:
    #print keys and values of the dictionary
    print(png_dict.keys())
    print(png_dict.values())


