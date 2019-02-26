
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
import json
import decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('greyhawk-calendar-data')

with open("data.json") as json_file:
    data = json.load(json_file, parse_float = decimal.Decimal)
    for info in data:
        MonthNumber = int(info['MonthNumber'])
        Month = info['Month']
        Day = int(info['Day'])
        DayOfWeek = info['DayOfWeek']
        Season = info['Season']
        Luna = info['Luna']
        Celene = info['Celene']
        Solstace = info['Solstace']
        Special = info['Special']



        # print("Adding records:", Month, Day)

        table.put_item(
           Item={
                "MonthNumber": MonthNumber,
                "Month": Month,
                "Day": Day,
                "DayOfWeek": DayOfWeek,
                "Season": Season,
                "Luna": Luna,
                "Celene": Celene,
                "Solstace": Solstace,
                "Special": Special
            }
        )
