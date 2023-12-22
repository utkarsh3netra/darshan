import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = 'querydata.csv'

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

# Now 'df' contains the data from the Excel sheet
print(df)
