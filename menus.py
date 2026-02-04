from auth import user_input, user_loading, authentication

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

def menu_meneger(filename):
    username, password = user_input()
    user_data = user_loading(filename)
    if authentication(username, password, user_data):
        return True
    else:
        return False    
        
        

    
    
    







        




