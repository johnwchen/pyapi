#!/usr/bin/env python3

import requests
import pprint



#http://www.omdbapi.com/?apikey=60a7479d&s=hulk

movies = requests.get("http://www.omdbapi.com/?apikey=60a7479d&s=hulk&type=movie")
print(len(movies.json()['Search']))

for i in range(len(movies.json()['Search'])):
    pprint.pprint(movies.json()['Search'][int(i)]['Title'])
    pprint.pprint(movies.json()['Search'][int(i)]['Type'])


#AA = movies.json()
#BB = AA['Search']
#pprint.pprint(BB[0]['Type'])