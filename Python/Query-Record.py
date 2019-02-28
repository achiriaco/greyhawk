import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('greyhawk-caledar-data')

response = table.get_item(
   Key={
        'Month': 'Richfest',
        'Day': '3'
    }
)

item = response['Item']
name = item['Month']

print(item)
print("Hello, {}" .format(name))