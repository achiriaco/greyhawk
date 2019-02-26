#Create Table


#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb')


table = dynamodb.create_table(
    TableName='greyhawk-calendar-data',
    KeySchema=[
        {
            'AttributeName': 'RecordName',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Month',
            'KeyType': 'RANGE'  #Sort key
        },
        {
            'AttributeName': 'Day',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'RecordName',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Month',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Day',
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print("Table status:", table.table_status)
