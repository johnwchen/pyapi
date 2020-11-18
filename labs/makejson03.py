#!/usr/bin/env python3

## Create a new script that can parse out our new JSON file

import json

def main():
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()
    
    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data. Python cannot easily work with this data.")
    #input("Press Enter to continue\n")            

    ## Create the JSON string
    datacenterdecoded = json.loads(datacenterstring)
    
    exit()


    ## This is now a dictionary
    print(type(datacenterdecoded))
    
    ## display the servers in the datacenter
    print(datacenterdecoded)
    
    ## display the servers in row3
    print(datacenterdecoded["row3"])
    
    ## display the 2nd server in row2
    print(datacenterdecoded["row2"][1])
    
    ## write code to
    ## display the last server in row3

if __name__ == "__main__":
    main()


