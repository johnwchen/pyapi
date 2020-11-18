#!/usr/bin/env python3


import requests
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    with open("nasa_apiKey.txt", "r") as API_KEY:
        API_KEY = API_KEY.read()
        API_KEY = "api_key=" + API_KEY.strip("\n")

        APOD_DATA = requests.get(NASAAPI + API_KEY)
        apod = APOD_DATA.json()
        print(apod)

if __name__ == "__main__":
    main()