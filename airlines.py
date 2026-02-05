import json


from load_checking_files import load_airport,load_budget,read_write_json
def menu_nwe_line():
    print("Choose if you want to add a new line.")
    manager = input("1.choose add a new line: 2.coose not add a new line:")
    if manager != "1":
        print("no add new line")
        exit()
    enter_code_origin = input("enter code origin ")
    enter_code_dest = input("enter code dest ")
    return enter_code_origin, enter_code_dest


def testing_line_budget(enter_code_origin, enter_code_dest):
    many_origin = 0
    many_dest = 0
    found = False
    for row in load_airport():
        if enter_code_origin in row:
            many_origin = int(row[5])
            for row in load_airport():
                if enter_code_dest in row:
                    many_dest = int(row[5])
                    found = True
                    break
            break
    if not found:
        print("one code not found enter other code")
    if load_budget() < float(many_origin + many_dest):
        print("has not enough budget")
    else:
        return True

def add_line_json(enter_code_origin, enter_code_dest):
    while True:
        approval = input("you sour add new line? (y/n):  ").lower()
        if approval == "y":
            new_list = read_write_json()
            new_list["available_lines"].append({'origin_airport': enter_code_origin, 'destination_airport': enter_code_dest})
            print(new_list)
            break
        elif approval == "n":
            exit()
        else:
            print("enter y or n")
    with open('available_flights.json', 'w', encoding='utf-8') as f:
        json.dump(new_list, f, ensure_ascii=False, indent=4)
code_oring, code_dest = menu_nwe_line()
test = testing_line_budget(code_oring, code_dest)
if test:
    add_line_json(code_oring, code_dest)
