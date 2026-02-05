from load_checking_files import files_exiest
from menus import check_user, manager_menu, client_menu
from auth import user_input, user_loading, authentication


def main():
    if files_exiest("credentials.csv") and files_exiest("budget.txt"):
        file_meneger = "credentials.csv"
        file_budget = "budget.csv"
        if check_user() == "menger":
            username, password = user_input()
            user_data = user_loading(file_meneger)
            if authentication(username, password, user_data):
                action_dict = {"1" : "", "2" : "", "3" : "", "4" : exit}
                user_action = manager_menu()
                action_dict[user_action]()
        else:
            action_dict = {"1" : "", "2" : ""}
            user_action = client_menu()
            # action_dict[user_action]()
    
    
           
           
main()