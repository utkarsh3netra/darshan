import boto3
import uuid
from datetime import datetime

def lambda_handler(event, context):
    # Set the DynamoDB table name
    dynamodb_table_name = 'YourDynamoDBTableName'

    # Parse the incoming event data (assuming it's a JSON payload)
    item_data = event.get('body')

    # Generate unique identifiers
    pk = str(uuid.uuid4())
    sk = 'ITEM#' + pk
    gsi_1_pk = 'CATEGORY#' + item_data['where_condition']
    gsi_1_sk = datetime.now().isoformat()

    # Create DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table_name)

    # Create item to be saved in DynamoDB
    item = {
        'pk': pk,
        'sk': sk,
        'GSI_1_pk': gsi_1_pk,
        'GSI_1_sk': gsi_1_sk,
        'name': item_data['name'],
        'description': item_data['description'],
        'where_condition': item_data['where_condition']
    }

    # Put item into DynamoDB table
    table.put_item(Item=item)

    # Return a response
    response = {
        'statusCode': 200,
        'body': 'Item saved successfully!'
    }

    return response









mutation createInternTestField($createinterntestfieldinput: CreateInternTestFieldInput!) {
  createInternTestField(input: $createinterntestfieldinput) {
    GSI_1_pk
    GSI_1_sk
    pk
    sk
  }
}

# After running createInternTestField, try running the listInternTestFields query.
query listInternTestFields {
  listInternTestFields {
    items {
      GSI_1_pk
      GSI_1_sk
      pk
      sk
    }
  }
}


"GSI_1_pk": "",
    "GSI_1_sk": "",

"sk": ""

query:
query listInternTestFields {
  listInternTestFields(filter: {pk: {eq: "Darshan#darshan"}, sk: {eq: "e17026377104805915c17026377104805915e17026377104805915m17026377104805915x"}}) {
    items {
      GSI_1_pk
      GSI_1_sk
      pk
      sk
    }
  }
}


query list{
  listInternTestFields{
    items{
      GSI_1_pk
      GSI_1_sk
      pk
      sk
    }
  }
}

query get{
  getInternTestField(pk: "Darshan#darshan"){
    sk GSI_1_pk GSI_1_sk
  }
}
