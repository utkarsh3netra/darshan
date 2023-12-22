import pandas as pd
import boto3

# Load data from Excel file into Pandas DataFrame
excel_file_path = 'path/to/your/excel/file.xlsx'
df = pd.read_excel(excel_file_path)

# Replace 'YourDynamoDBTableName' with the actual name of your DynamoDB table

# Convert DataFrame to a list of dictionaries (each dictionary represents a row)
data_to_insert = df.to_dict(orient='records')

# Initialize AWS DynamoDB client
table = boto3.resource('dynamodb',
                       aws_access_key_id="ASIAYNQHBUMHTVL5BR6Y",
                       aws_secret_access_key="M1UALPhy8eCdjumEXaGXk3NyY49fZ+Q0dwEAvteQ",
                       aws_session_token="IQoJb3JpZ2luX2VjEFQaCXVzLWVhc3QtMSJHMEUCIEhPlCUHcgrs9kDAJt/bznyInsD8Jxfn54E4xWeHH3vzAiEApIzw0he3qdh5OUOKVwopx4hbhrCvE6rASF7W4i8os8oqgwMIzf//////////ARAAGgw1Nzg3NjE2MzA0NzkiDI2YNjYbBr6oeh+7TirXAsf2JI1Q4d8SYyfo8HjvlQAuXwliPrx51z03JdGS7EhWRKRmk1hccvVuvxo0HfrJFWpPslCzDVqkdIQ1ofP6UboQILtumwTj6hh/abAcHiWtzFAq3TrlEoJAwN4FMHN6+XopxvvTlrjrwgEjkdmjsgbWExS072a6YcXIru8tpQXQrbqPsnHDtvd/+fQSqHpd9IWl18fcHIX0jJoijUnj9+WNz3BD0oLGTJsCp7HaodeSEQLj2/AL0dgoxq2dRBUOTwwD8jF6Xhi9kcVtPIWoCRU/1IHkqg6vrRQ9vViUgp29E+DMUsTpiFY3mXnXunUfnHBae0KF4fSwv5U1g7QIkPWKyKkARqeBM+oHlQoNYPtXI+kwDUu4yXkeuE/ctKWOO5Ow8cW1HDdX+KOm+zB28IvQRrprC/bJ7JFvxVcI8FBT9+DyzIbckKHn/urTyE5SZKs1AkoESz0w+Z6ErAY6pwEFIJzv8q66Wj/W0/ZC2XGqleTqupSjVcJ3T+w/Bso+CZegwDDFM2S4LyGotctQpU3nyuMY85J0E7mh9VWaowwXeBaSLum+rmDe0oySen7PDQE4W9KKl5iMRogIhAuuOXQd4WIj8M7XU/nsVD6tQvhA/znnZzcnxmjtS2Aa2QzvEW+DOkJ9ekCrTUtHDCCwZvmwqRRz4vKpGks34vE30dS+iXdJZgQhAw=="
                       ).Table('InternTestField')

# Batch write items to DynamoDB table
with table.batch_writer() as batch:
    for item in data_to_insert:
        batch.put_item(Item=item)

print("Data inserted into DynamoDB table successfully.")
