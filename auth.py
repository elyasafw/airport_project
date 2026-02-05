import csv, sys


def user_loading(filename):
    matrix = []
    with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                matrix.append(row)
            return matrix
    
def authentication(username, password, matrix):
    print("please enter your username and password")
    for user in matrix:
        if user[0] == username and user[1] == password:
            print("Welcome " + username)
            return True    
    print("Invalid username or password")
    exit()



def user_input():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password



            


