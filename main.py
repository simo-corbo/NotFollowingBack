# Small Python script to see who doesn't follow you back on instagram
import json

if __name__ == '__main__':
    # Opening JSON file
    f = open('followers.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['emp_details']:
        print(i)

    # Closing file
    f.close()