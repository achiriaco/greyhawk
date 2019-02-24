# Program steps
# 1. Input of what Month
# 2. Input of what day
# 3. Load JSON file data.JSON
# 4. Find the keypairs for the month and date
import json

# json_string = '{"Month": "Sunsebb",, "Day": 22}'


# parsed_json = json.loads(json_string)

# print (parsed_json["Month"])


with open('data.json', 'r') as fp:
    json_data = json.load(fp)


month = json_data["Month"]
day = json_data["Day"]



# for distro in distros_dict:
#     print(distro['Month'])

# for item in json_data:
#     print item.get("Month").get("Day")