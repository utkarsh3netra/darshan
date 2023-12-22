
table_name = "InternTestField"
dynamodb = boto3.resource('dynamodb')


def create_table():
    table = dynamodb.create_table(
        TableName='InternTestFiel_ddarshan',
        KeySchema=[
            {
                'AttributeName': 'pk',
                'KeyType': 'HASH'  # HASH For Partition Key
            },
            {
                'AttributeName': 'sk',
                'KeyType': 'RANGE'  # RANGE For Sort Key
            }
        ],

        AttributeDefinitions=[
            {
                'AttributeName': 'pk',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'sk',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1000,
            'WriteCapacityUnits': 1000
        }

    )

    
def query_by_id(id_value):
    filtering_exp = Key('id').eq(id_value)
    response = employee.query(
        KeyConditionExpression=filtering_exp
    )
    for item in response['Items']:
        print(f'{item}')


def queryid_and_fname(id_value, fname_value):
    filtering_exp = Key('id').eq(id_value)
    filtering_exp1 = Key('fname').eq(fname_value)
    response = employee.query(
        KeyConditionExpression=filtering_exp & filtering_exp1
    )
    for item in response['Items']:
        print(f'{item}')


def update():
    response = employee.update_item(
        Key={
            'id': 1,
            'fname': 'darshan'
        },
        UpdateExpression='SET #lname= :r',
        ExpressionAttributeValues={
            ':r': 'AAAA'
        },
        ExpressionAttributeNames={
            '#lname': 'lname'
        },
        ReturnValues='UPDATED_NEW'
    )

    print(f'{response}')


def delete():
    response = employee.delete_item(
        Key={
            'id': 4,
            'fname': 'HHHH'
        }
    )
    print(f'{response}')


def delete_many(items_to_delete):
    with employee.batch_writer() as batch:
        for item in items_to_delete:
            batch.delete_item(
                Key={
                    'id': item['id'],
                    'fname': item['fname']
                }
            )


# items = [{"id": 5, 'fname': 'AAAA'},{"id": 2, 'fname': 'BBBB'},{"id": 2, 'fname': 'CCCC'}]

def delete_table():
    employee.delete()


# create_table()
# insert()
# query_by_id(2)
# queryid_and_fname(1, 'darshan')
# update()
# delete()
# delete_many(items)
# delete_table()