from pprint import pprint

import pandas as pd
import boto3
from decimal import Decimal,ROUND_HALF_UP
import numpy as np
import json

excel_file = 'E:\Darshan\AppSync\querydata.csv'
df = pd.read_csv(excel_file)
# df.info()

table = boto3.resource('dynamodb',
                       aws_access_key_id="ASIAYNQHBUMHWZCNYMZZ",
                       aws_secret_access_key="SNa21TV+blUGgTwUW+uGCjVwj0YJl03TiZwXgTh0",
                       aws_session_token="IQoJb3JpZ2luX2VjEG0aCXVzLWVhc3QtMSJIMEYCIQDsaTL/SpVy+89RrnU5wl4JWuFurofTY58Txcai+CtfXQIhAJfJxDmukS41CIRBBNagEC/FUtnCFkNA/5lZm1FN9gAhKoMDCOX//////////wEQABoMNTc4NzYxNjMwNDc5IgxqPPQsuj+MUyHqvcoq1wK9E94GloKpnk4OAFn0JI1vTU5hC5sRWHIBgZ2tfnOaIN+nz6qhPjtegWOOK2+04CclEiOP691M/7H2iew4nwJBae1HSwfhH610JbtEk+TlGszbtQIZyHd4ic13tW4bTW0kdWqPbAivK9JBAqV8disrCMPRpXtJevUdsvzOAI5BDR0UULUGB2Xj2PUeHLXsWWsbEjPgxoKdhCpeXe1mJ4FtrdPivq55yqTztPOJ8bUJbPwSXoecJGFEWThA8QULJkMiqCadY2Vw8b1CdrH2P/mZa0s+lL5Q8ECdumTqmkDf/cdXAa0eB1M9Z7LZGEgNkVfObPvL14SW8Wcy6mRrqE51/PGovTP7yZiZ7EveeIOJQxBmoHHQHhinvOBOoo11U9Nf0KeKTnbqat9GmKUI+YrdXteByKB7PBKB5gIDZf2+270o5Hc1EC5ClDjxfd8wc9kAsRNtEDuhMIPSiawGOqYB6nC+jB4yt4y4WU0LYa9mmp5XRf8Hq0n+lIve3sZap6xFWckgKmNkeYnODVAn5Ld+YWuvWuGxvFzgV4D3WbHFkWNrw8HbagrrgsBECA3q9BtX7JfokNxud8lg+mkXdlOVIamujUtjlK9Oxh3cP9JzoZlsnS1mcu5iqR80wE/IJHif18HTgnd8BTHudrQuIxbWuQnX3Wswbx94MNGrmaANTpcrBDrFIw=="
                       ).Table('AppSync-Demo-Athena')

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

df['account_number'] = df['account_number'].apply( str)
df['prop_state'] = df['prop_state'].apply( str)
df['new_pi_savings_mo_refi'] = df['new_pi_savings_mo_refi'].apply( lambda i: Decimal(i))
df['new_cashout_refi'] = df['new_cashout_refi'].apply( lambda i: Decimal(i))
df['new_pi_savings_mo_co'] = df['new_pi_savings_mo_co'].apply( lambda i: Decimal(i))
df['new_cashout_co'] = df['new_cashout_co'].apply( lambda i: Decimal(i))
df['new_pi_savings_mo_pf'] = df['new_pi_savings_mo_pf'].apply( lambda i: Decimal(i))
df['new_product_description_co'] = df['new_product_description_co'].apply( str)
insert = df.to_dict(orient='records')

# insert = df.isnull = ""

# print(df.dtypes)


#with table.table() as batch:
for item in insert:
    try:
        item.items()
        #item = {'Value': {'NULL': True}, 'Action': 'PUT'}
        #item={'value': 0}
        item = {k: v for k, v in item.items() if v is not np.nan and v != np.inf and v != -np.inf}
        table.put_item(Item=item)
    except Exception as e :
        print("error".center(90,"*"))
        print(e)
        pprint(item)
        for key,values in item.items():
            print(key,values)
            pprint(type(values))
        break

#with table.batch_writer() as batch:
#    for item in insert:
#        item_to_put: dict = json.loads(json.dumps(item), parse_float=Decimal)

        # Send record to database.
        #batch.put_item(Item=item_to_put)
print("Data inserted into DynamoDB table successfully.")

