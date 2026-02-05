from load_checking_files import files_exiest
from menus import menu_meneger, check_user
from auth import user_input, user_loading, authentication

if files_exiest("credentials.csv") and files_exiest("budget.txt"):
 filename_meneger = "credentials.csv"
 filename_budget = "budget.csv"
else:
    exit()

def main():
    print("please enter your choice:")
    if check_user() == "menger":
        print("welcome to meneger")
        print("please enter your username and password")
        username, password = user_input()
        user_data = user_loading(filename_meneger)
        print(user_data)
        print(username, password)
        if authentication(username, password, user_data):
           print("login success")
        else:
           print("eror")
           exit()
        
main()

           
         
          
