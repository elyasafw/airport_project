def check_user():
    print("1.manager \n2.client \n")
    while True:
        user = input("manager  enter 1:  client enter 2:")
        if user == "1":
            return "menger"
        elif user == "2":
            return "client"
        else:
            print("please enter 1 or 2")

