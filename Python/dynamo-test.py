import boto3

dynamodb_client = boto3.client('dynamodb')
dynamodb_resource = boto3.resource('dynamodb')

dynamodbTable = 'mytablename'

tables = dynamodb_client.list_tables()

if dynamodbTable in tables['TableNames']:
	if DEBUG: print('DynamoDB table ' +  dynamodbTable + ' exists')
else:
	create_table(dynamodbTable)
	if DEBUG: print("Created table" + dynamodbTable)
	table = dynamodb_resource.Table(dynamodbTable)

def create_table(table_name):
    dynamodb_client.create_table(
            TableName=table_name,
            AttributeDefinitions=[
                {
                    'AttributeName': 'UserId',
                    'AttributeType': 'S'
                },
            ],
            KeySchema=[
                {
                    'AttributeName': 'UserId',
                    'KeyType': 'HASH'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    table = dynamodb_resource.Table(table_name)
    table.wait_until_exists()

def initSession(session):
	response = table.get_item(
		Key={
			'UserId': session['user']['userId']
		}
		)
	if 'Item' in response:
		if DEBUG: print("Existing userId. Item:")
		if DEBUG: print(response['Item'])
		
		if "session" in response['Item']:
			return response['Item']['session']
		else:
			return False
	else:
		table.put_item(
			Item={
				'UserId': session['user']['userId']
			}
		)
		return False