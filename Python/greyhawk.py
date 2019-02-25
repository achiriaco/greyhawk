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
inputmonth = "Richfest"
inputday = 4

def read_json(path):
    with open(path, 'r') as fp:
        # convert string to python object
        json_data = json.load(fp)
        for result in json_data:
            if result['Month'] == inputmonth:
                if result['Day'] == inputday:
                    Month = result["Month"]
                    Day = result["Day"]
                    DayOfWeek = result["DayOfWeek"]
                    Season = result["Season"]
                    Luna = result["Luna"]
                    Celene = result["Celene"]
                    Solstace = result["Solstace"]
                    Special = result["Special"]
                    print("The Month is: " + Month )
                    print("The Day is: " + str(Day) )
                    print("The Day of the Week is: " + DayOfWeek)
                    print("The Season is: " + Season)
                    print("The Moon Luna is: " + Luna)
                    print("The Moon Celene is: " + Celene)
                    if not Solstace == "":
                        print("The Solstace is: " + Solstace)
                    if not Special == "":
                        print(Special)
                                       

'''if name == main is for running code when it is the main module. This code will not run if this module gets imported, it is good for keeping test code without running when importing'''
if __name__ == '__main__':
    # execute running the file here if running from this page
    print(read_json(path))