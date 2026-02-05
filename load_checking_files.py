from pathlib import Path
import csv

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
