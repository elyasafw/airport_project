from load_checking_files import files_exiest
from menus import check_user
from auth import user_input, user_loading, authentication

if files_exiest("credentials.csv") and files_exiest("budget.txt"):
 file_meneger = "credentials.csv"
 file_budget = "budget.csv"
else:
    exit()

def main():
    if check_user() == "menger":
        username, password = user_input()
        user_data = user_loading(file_meneger)
        if authentication(username, password, user_data):
           pass
    
           
           
main()


           
         
          