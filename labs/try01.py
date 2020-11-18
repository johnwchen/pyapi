#!/usr/bin/env python3

while True: 
    try:
        print("Enter a file name. ")
        name = input()
        with open(name, 'w') as newfile:
            newfile.write("No problems with that file name.")
        break
    except:
        print("error with that file name!..try again")

        