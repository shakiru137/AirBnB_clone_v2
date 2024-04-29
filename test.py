#!/usr/bin/python3
import sqlalchemy
attr = (dir(sqlalchemy))
string = 'create_engine'
for arg in attr:
    if string == arg:
        print(f"{arg} is foung")
    
print("END")
