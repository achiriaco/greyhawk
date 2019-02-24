# Program steps
# 1. Input of what Month
# 2. Input of what day
# 3. Load JSON file data.JSON
# 4. Find the keypairs for the month and date
import json

# json_string = '{"Month": "Sunsebb",, "Day": 22}'


# parsed_json = json.loads(json_string)

# print (parsed_json["Month"])

path = "data.json"

def read_json(path):
    with open(path, 'r') as fp:
        # convert string to python object
        json_data = json.load(fp)
        # in the json dictionary we have many dicitonaries in a list
        # iterate through the list
        for dictionaires in json_data:
            # for each ditionary print the keys
            print(dictionaires.keys())
            # for each dictionary print this key
            print(dictionaires['Month'])
            # here we are assignin the key month to this variable
            # caution however as ever new iterated dictionary will overwrite the prvious entry
            month = dictionaires["Month"]

            day = dictionaires["Day"]

'''i imagine youl need to do some sort of if condition here and if successful you would return the dictionary like so

        if input == month:
            return dictionaries

this will return that one dictionary or json object to the client'''


# for distro in distros_dict:
#     print(distro['Month'])

# for item in json_data:
#     print item.get("Month").get("Day")

'''if name == main is for running code when it is the main module. This code will not run if this module gets imported, it is good for keeping test code without running when importing'''
if __name__ == '__main__':
    # execute running the file here if running from this page
    print(read_json(path))
    