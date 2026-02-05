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
    

def load_airport (filnam_csv):
    airlines = filnam_csv
    if files_exiest(airlines):
        with open(airlines, 'r', encoding='utf-8') as f:
            airlines_list = []
            for row in csv.reader(f):
                airlines_list.append(row)
            return airlines_list


def flight_list(file_json):
    with open(file_json, 'r', encoding='utf-8') as f:
        airlines_data = json.load(f)
        airlines_data = airlines_data["available_lines"]
        origin_code = airlines_data[0]["origin_airport"] 
        destination_code = airlines_data[0]["destination_airport"]
    return [origin_code, destination_code]



def read_json(json_file):
    if files_exiest(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
 

def airport_cod_city(airport_code, airport_data):
    for airport in airport_data:
        if airport[0] == airport_code:
            airport_name = airport[2]
            return airport_name


def buying_client(flights_data, airpor_data):
    print("--- flight list ---")
    for i in range(1, len(flights_data)):
        origin = airport_cod_city(flights_data[0], airpor_data)
        dest = airport_cod_city(flights_data[1], airpor_data)
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



def Flight_price_calculation(origin, destination, airport_data):
    for airport in airport_data:
        if airport[0] == origin:
            price = int(airport[5])
            
        

        
        
         