import pandas as pd
import boto3

# Load data from Excel file into Pandas DataFrame
excel_file_path = 'path/to/your/excel/file.xlsx'
df = pd.read_excel(excel_file_path)

# Replace 'YourDynamoDBTableName' with the actual name of your DynamoDB table

# Convert DataFrame to a list of dictionaries (each dictionary represents a row)
data_to_insert = df.to_dict(orient='records')

# Initialize AWS DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourDynamoDBTableName')

# Batch write items to DynamoDB table
with table.batch_writer() as batch:
    for item in data_to_insert:
        batch.put_item(Item=item)

print("Data inserted into DynamoDB table successfully.")
