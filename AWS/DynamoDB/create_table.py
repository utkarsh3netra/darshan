import time

import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
import random
import string

table = boto3.resource('dynamodb',
                       aws_access_key_id="ASIAYNQHBUMHTVL5BR6Y",
                       aws_secret_access_key="M1UALPhy8eCdjumEXaGXk3NyY49fZ+Q0dwEAvteQ",
                       aws_session_token="IQoJb3JpZ2luX2VjEFQaCXVzLWVhc3QtMSJHMEUCIEhPlCUHcgrs9kDAJt/bznyInsD8Jxfn54E4xWeHH3vzAiEApIzw0he3qdh5OUOKVwopx4hbhrCvE6rASF7W4i8os8oqgwMIzf//////////ARAAGgw1Nzg3NjE2MzA0NzkiDI2YNjYbBr6oeh+7TirXAsf2JI1Q4d8SYyfo8HjvlQAuXwliPrx51z03JdGS7EhWRKRmk1hccvVuvxo0HfrJFWpPslCzDVqkdIQ1ofP6UboQILtumwTj6hh/abAcHiWtzFAq3TrlEoJAwN4FMHN6+XopxvvTlrjrwgEjkdmjsgbWExS072a6YcXIru8tpQXQrbqPsnHDtvd/+fQSqHpd9IWl18fcHIX0jJoijUnj9+WNz3BD0oLGTJsCp7HaodeSEQLj2/AL0dgoxq2dRBUOTwwD8jF6Xhi9kcVtPIWoCRU/1IHkqg6vrRQ9vViUgp29E+DMUsTpiFY3mXnXunUfnHBae0KF4fSwv5U1g7QIkPWKyKkARqeBM+oHlQoNYPtXI+kwDUu4yXkeuE/ctKWOO5Ow8cW1HDdX+KOm+zB28IvQRrprC/bJ7JFvxVcI8FBT9+DyzIbckKHn/urTyE5SZKs1AkoESz0w+Z6ErAY6pwEFIJzv8q66Wj/W0/ZC2XGqleTqupSjVcJ3T+w/Bso+CZegwDDFM2S4LyGotctQpU3nyuMY85J0E7mh9VWaowwXeBaSLum+rmDe0oySen7PDQE4W9KKl5iMRogIhAuuOXQd4WIj8M7XU/nsVD6tQvhA/znnZzcnxmjtS2Aa2QzvEW+DOkJ9ekCrTUtHDCCwZvmwqRRz4vKpGks34vE30dS+iXdJZgQhAw=="
                       ).Table('InternTestField')

def name():
    testwriter_name = "Darshan"
    return testwriter_name


def rndmsk():
    timesk = str(time.time()).replace(".", "")
    skname = string.ascii_lowercase
    skid = f"{timesk}".join(random.choice(skname) for i in range(6))
    return skid
sk_value = rndmsk()

def insert():
    response = table.put_item(
        Item={
            'pk': f'{name()}#{name().lower()}',
            'sk': sk_value,
            'name': 'segment 5',
            'description': 'test Segment 5',
            'where_condition': 'segment==1',
            'GSI_1_pk': f'{name()}#{datetime.now().strftime('%Y/%m')}',
            'GSI_1_sk': sk_value,
            'current_time': datetime.now().isoformat(),
            'update_time': " "
        }
    )
    print(f'Insert response : {response}')


# insert()

def query_pk_and_sk(pk_value, sk_value):
    filtering_exp = Key('pk').eq(pk_value)
    filtering_exp1 = Key('sk').eq(sk_value)
    response = table.query(
        KeyConditionExpression=filtering_exp & filtering_exp1
    )
    for item in response['Items']:
        print(f'{item}')


query_pk_and_sk('Darshan#darshan','z')

def query_gsi(gsi_1_pk_value):
    filtering_exp = Key('GSI_1_pk').eq(gsi_1_pk_value)
    response = table.query(
        IndexName='GSI_1',
        KeyConditionExpression="GSI_1_pk= :val",
        ExpressionAttributeValues={
            ":val": gsi_1_pk_value
        }
    )

# query_gsi('Darshan#2023/12')

def update():
    response = table.update_item(
        Key={
            'pk': 'Darshan#darshan',
            'sk': 'q1702892174731734s1702892174731734k1702892174731734i1702892174731734z1702892174731734i'
        },
        UpdateExpression='SET #description= :r,#update_time= :d',
        ExpressionAttributeValues={
            ':r': 'updated test segment',
            ':d': datetime.now().isoformat()
        },
        ExpressionAttributeNames={
            '#description': 'description',
            '#update_time': 'update_time'
        },
        ReturnValues='UPDATED_NEW'
    )

    print(f'{response}')


# update()
