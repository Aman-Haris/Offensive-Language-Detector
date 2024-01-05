import pandas as pd

csv_file1_path = 'english.csv'
csv_file2_path = 'kannada.csv'

# Reading the CSV files into pandas DataFrames
df1 = pd.read_csv(csv_file1_path, encoding='latin1')
df2 = pd.read_csv(csv_file2_path, encoding='latin1')

#combining english and kannada data csv into one csv
combined_df = pd.concat([df1, df2], ignore_index=True)

combined_csv_file_path = 'Data.csv'

# Saving the combined DataFrame to a new CSV file
combined_df.to_csv(combined_csv_file_path, index=False)

#Checking final data file
csv_file3_path = 'Data.csv'
df3 = pd.read_csv(csv_file3_path, encoding='latin1')
uv = df3['is_offensive'].unique()
# Print the unique values
print(uv)