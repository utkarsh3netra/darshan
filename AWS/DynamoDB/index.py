from boto3 import resource
from boto3.dynamodb.conditions import Key
from datetime import datetime

demo_table = resource('dynamodb').Table('demo-try-python')

def insert():
    print(f'demo_insert')
    response = demo_table.put_item(
        Item={
            'customer_id': 'cus-01',  # parition key
            'order_id': 'ord-04',  # sort key
            'status': 'pending',
            'created_date': datetime.now().isoformat()
        }
    )
    print(f'Insert response: {response}')


def query_by_partition_key(customer_value):
    print('demo_select_query')

    filtering_exp = Key('customer_id').eq(customer_value)
    response = demo_table.query(
        KeyConditionExpression=filtering_exp,
        ScanIndexForward=False)
    item_list = response["Items"]
    for item in item_list:
        print(f'Item: {item}')


def query_by_index_key(status_value):
    filtering_exp = Key('status').eq(status_value)
    response = demo_table.query(
        IndexName='status-index',
        KeyConditionExpression=filtering_exp,
        ScanIndexForward=False)

    for item in response['Items']:
        print(f'Item: {item}')


def query_by_partition_key_and_sort_key(customer_value, order_value):
    filtering_exp1 = Key('customer_id').eq(customer_value)
    filtering_exp2 = Key('order_id').eq(order_value)
    response = demo_table.query(
        KeyConditionExpression=filtering_exp1 & filtering_exp2)

    for item in response['Items']:
        print(f'Item: {item}')


def updet(customer_value, order_value, status_value):
    response = demo_table.update_item(
        Key={
            'customer_id': customer_value,
            'order_id': order_value
        },
        UpdateExpression='set #status=:r, update_date=:d',
        ExpressionAttributeValues={
            ':r': status_value,
            ':d': datetime.now().isoformat()
        },

        ExpressionAttributeNames={
            '#status': 'status'
        },
        ReturnValues='UPDATED_NEW'
    )
    print(f'Reponse: {response}')


def delete(items_to_delete):
    with demo_table.batch_writer() as batch:
        for item in items_to_delete:
            batch.delete_item(
                Key={
                    'customer_id': item['id'],
                    'order_id': item['order_id']
                }
            )


items = [{"id": 'cus-01', 'order_id': 'ord-04'}]
# delete(items)
insert()
query_by_partition_key('cus-01')
query_by_partition_key_and_sort_key('cus-01', 'ord-02')
query_by_index_key('completed')
updet('cus-01', 'ord-02', 'completed')
# items = [{"id": 'cus-01', 'order_id': 'ord-04'}]
# delete(items)
