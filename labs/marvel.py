#!/usr/bin/env python3

import requests

def main():
    action_hero = requests.get("https://gateway.marvel.com:443/v1/public/characters?name=spider-man&apikey=138da81c8aa63c4122421ee485039deb")
    print(action_hero)


if __name__ == "__main__":
    main()