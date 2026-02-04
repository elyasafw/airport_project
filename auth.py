import csv


def user_loading(filename):
    matrix = []
    with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                matrix.append(row)


def authentication(username, password, matrix):
    for user in matrix:
        if user[0] == username and user[1] == password:
            return True
    return False

def user_input():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password
            
