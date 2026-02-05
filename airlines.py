import json
from load_checking_files import read_json, load_airport, load_budget, update_budget
from menus import new_line_menu

def budget_check_codes(origin_code, dest_code):
    origin_prine = 0
    dest_price = 0
    found = False
    airport_list = load_airport("./airport_entry_fee.csv")
    for row in airport_list:
        if origin_code in row:
            origin_prine = int(row[5])
            for row in airport_list:
                if dest_code in row:
                    dest_price = int(row[5])
                    found = True
                    break
            final_price = float(origin_prine + dest_price)
            print(f"\nA match was found for the flight codes you selected. | The cost of establishing the flight line is: {final_price}")
            break
    if not found:
        print("\nNo origin / destination code found..")
    budget = load_budget()
    if budget < final_price:
        print(f"\nYour budget is: {budget} You don't have enough budget..")
    else:
        print("\nGreat, you have enough budget.")
        final_budget = budget - final_price
        return True, final_budget


def add_flight_line(origin_code, dest_code):
    while True:
        approval = input("\nAre you sure you want to add a new flight route? (y/n):  ").lower()
        if approval == "y":
            flights_available = read_json("./available_flights.json")
            flights_available["available_lines"].append({'origin_airport': origin_code, 'destination_airport': dest_code})
            break
        elif approval == "n":
            exit()
        else:
            print("Please select only y / n")
    with open('available_flights.json', 'w', encoding='utf-8') as f:
        json.dump(flights_available, f, ensure_ascii=False, indent=4)
        print("\nThe list of available flights has been successfully updated!")
        return True


def play_add_line():
    origin_code, dest_code =  new_line_menu()
    is_approved, final_budget = budget_check_codes(origin_code, dest_code)
    if is_approved:
        is_added = add_flight_line(origin_code, dest_code)
        if is_added:
            update_budget(final_budget)