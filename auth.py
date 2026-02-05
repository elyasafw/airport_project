import csv


def user_loading(file):
    users_list = []
    with open(file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                users_list.append(row)
            return users_list
    
def authentication(username, password, users_list):
    for user in users_list:
        if user[0] == username and user[1] == password:
            print("Manager login successful")
            return True
         
    exit("Login failed! System is closing..")


def user_input():
    username = input("Please enter your username:  ")
    password = input("Please enter your password:  ")
    return username, password