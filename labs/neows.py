#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("nasa_apiKey.txt", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=2015-09-07"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"
    enddate = "end_date=2015-09-08"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata["near_earth_objects"].keys())
    for date in neodata["near_earth_objects"].keys():
        for neo in neodata['near_earth_objects'][date]:
            print(neo['name'])
    
    

if __name__ == "__main__":
    main()

