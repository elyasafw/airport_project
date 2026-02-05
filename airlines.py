import csv, json
import json
from load_checking_files import load_airport,load_budget,read
def nwe_line():
    print("Choose if you want to add a new line.")
    manager = input("1.choose add a new line 2.coose not add a new line")
    if manager == "1":
        enter_code_origin = input("enter code origin ")
        enter_code_dest = input("enter code dest ")
        many_origin = 0
        many_dest = 0
        for row in load_airport():
            if row[0] == enter_code_origin:
                many_origin = row[5]
            elif row[0] == enter_code_dest:
                many_dest = row[5]
                if load_budget() - many_origin and load_airport()- many_dest < 0:
                    print("has not enough budget")
                else:
                    true =  input("you sour add new line ? if yes click 1")
                    if true == "1":
                        with open('available_flights.json','a') as f:
                            write()
            elif enter_code_origin or enter_code_dest not in row[0]:
                print("one code not found enter other code")
