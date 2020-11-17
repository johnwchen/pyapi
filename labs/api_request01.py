#!/usr/bin/env python3

import requests

ROCKETS = "http://api.open-notify.org/astros.json"

def getrocketman():
    getname = requests.get(ROCKETS).json()
    total_people = getname['number']
    print(f"There are total of {total_people} astronouts")
    print("Below are there names beging with:")

    count = 1
    for astro in getname['people']:
        #print(count)
        craft = astro['craft']
        print(f"{count}. {astro['name']} on the {craft}")
        count +=1

if __name__ == "__main__":
    getrocketman()

