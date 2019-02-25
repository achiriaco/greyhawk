import boto3

dynamodb=boto3.resource("dynamodb")
dynamoTable=dynamodb.Table("greyhawk_calendar_data")

table = dynamodb.Table('greyhawk_calendar_data')
print(table.creation_date_time)
table.put_item(
    Item={[{
            "RecordName": 1,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 1,
            "DayOfWeek": "Starday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "New Moon",
            "Celene": "Full Moon",
            "Solstace": "None",
            "Special": "None"
        }
        ,
        {
            "RecordName": 2,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 2,
            "DayOfWeek": "Sunday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "New Moon",
            "Celene": "Full Moon",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 3,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 3,
            "DayOfWeek": "Moonday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "New Moon Fading",
            "Celene": "Full Moon",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 4,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 4,
            "DayOfWeek": "Godsday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "New Moon Fading",
            "Celene": "Full Moon Fading",
            "Solstace": "The Winter Solstice is the shortest day of the year.",
            "Special": "None"
        },
        {
            "RecordName": 5,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 5,
            "DayOfWeek": "Waterday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "Waxing Crescent",
            "Celene": "Full Moon Fading",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 6,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 6,
            "DayOfWeek": "Earthday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "Waxing Crescent",
            "Celene": "Full Moon Fading",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 7,
            "MonthNumber": 1,
            "Month": "Needfest",
            "Day": 7,
            "DayOfWeek": "Freeday",
            "Season": "This frigid seven-day period marks the transition from one calendar year to another, and is usually accounted as the start of the new year.",
            "Luna": "Waxing Crescent Fading",
            "Celene": "Full Moon Fading",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 8,
            "MonthNumber": 2,
            "Month": "Fireseek",
            "Day": 1,
            "DayOfWeek": "Starday",
            "Season": "Winter",
            "Luna": "First Quarter",
            "Celene": "Full Moon Fading",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 9,
            "MonthNumber": 2,
            "Month": "Fireseek",
            "Day": 2,
            "DayOfWeek": "Monday",
            "Season": "Winter",
            "Luna": "First Quarter",
            "Celene": "Full Moon Fading",
            "Solstace": "None",
            "Special": "None"
        },
        {
            "RecordName": 10,
            "MonthNumber": 2,
            "Month": "Fireseek",
            "Day": 3,
            "DayOfWeek": "Moonday",
            "Season": "Winter",
            "Luna": "First Quarter Fading",
            "Celene": "Waning Gibbous",
            "Solstace": "None",
            "Special": "None"
        }]
    )