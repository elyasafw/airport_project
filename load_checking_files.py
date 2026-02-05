from pathlib import Path
import csv, json

def files_exiest(filename):
    file_path = Path(filename)
    if file_path.exists():
        return True
    else:
        print("error! file not found...")
        return False
    

def load_budget():
    with open('./budget.txt', 'r', encoding='utf-8') as f:
        return float(f.read())
    

def load_airport ():
    airlines = "./airport_entry_fee.csv"
    if files_exiest(airlines):
        with open(airlines, 'r', encoding='utf-8') as f:
            airlines_list = []
            for row in csv.reader(f):
                airlines_list.append(row)
            return airlines_list
        

def read_json():
    available_flights = "./available_flights.json "
    if files_exiest(available_flights):
        with open(available_flights, 'r', encoding='utf-8') as f:
            airlines_list = json.load(f)
            return airlines_list