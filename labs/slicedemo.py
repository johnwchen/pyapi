#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def chal(challenge):
    gog = challenge[2][0]
    eye = challenge[2][1]
    noth = challenge[3]
    print(f"My {eye}! The {gog} do {noth}")

def tri(trail):
    eye = trail[2]['goggles']
    gog = trail[2]['eyes']
    noth = trail[3]
    print(f"My {eye}! The {gog} do {noth}")

def night(nightmare):
    eye = nightmare[0]['user']['name']['first']
    gog = nightmare[0]['kumquat'] 
    noth = nightmare[0]['d'] 

    print(f"My {eye}! The {gog} do {noth}")
    #noth = 


if __name__ == "__main__":
    chal(challenge)
    tri(trial)
    night(nightmare)