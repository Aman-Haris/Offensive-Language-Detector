import pandas as pd 
import glob 
import os 

# merging the files 
joined_files = os.path.join("D:\Offensive Language Detector\Data", "k*.csv") 

# A list of all joined files is returned 
joined_list = glob.glob(joined_files) 

#files are joined using pandas
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True) 

#removing unwanted row
df1 = df[df['is_offensive'] != 'not-Kannada']

#changing the value of classifier column from text to 0-1
value_mapping = {
    'Not_offensive': '0',
    'Offensive_Targeted_Insult_Group': '1',
    'Offensive_Targeted_Insult_Other': '1',
    'Offensive_Targeted_Insult_Individual': '1',
    'Offensive_Untargetede': '1',
}

df2 = df1.replace(value_mapping)

#cross checking the data
uv = df2['is_offensive'].unique()
# Print the unique values
print(uv)

#csv_file_path = 'kannada.csv'
# Save the DataFrame to a CSV file
#df2.to_csv(csv_file_path, index=False)