def check_user():
    print("1. manager \n2. client \n")
    while True:
        user = input("please Choose Manager or Client (1/2):  ")
        if user == "1":
            return "menger"
        elif user == "2":
            return "client"
        else:
            print("please enter only 1 / 2")


def manager_menu():
    print("Welcome to the management menu\n1. Show available airlines\n2. Buying a new airline\n3. Show available budget\n4. exit")
    while True:
        manager_choise = input("Select desired action:  ")
        if manager_choise not in ["1", "2", "3", "4"]:
            print("Please choose only between 1 - 4")
        return manager_choise