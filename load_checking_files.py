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
        

def read_write_json():
    available_flights = "./available_flights.json "
    if files_exiest(available_flights):
        with open(available_flights, 'r', encoding='utf-8') as f:
            airlines_list = json.load(f)
            return airlines_list


def flight_list():
    with open('available_flights.json', 'r', encoding='utf-8') as f:
        airlines_data = json.load(f)
        return airlines_data.get("available_lines", [])

flight = flight_list()

all_flights = flight_list()

def buying_client(flights_data):
    print("--- flight list ---")
    for i, flight in enumerate(flights_data, 1):
        origin = flight['origin_airport']
        dest = flight['destination_airport']
        print(f"{i}. {origin} -> {dest}")
    
    vlide = False
    choice_num = 0 
    
    while not vlide:
        choice = input("Enter your choice: ")        
        if choice.isdigit():
            choice_num = int(choice) 
            
            if 1 <= choice_num <= len(flights_data):
                vlide = True
            else:
                print(f"please enter a number between 1 and {len(flights_data)}")
        else:
            print("please enter a number")
            
    return flights_data[choice_num - 1]



