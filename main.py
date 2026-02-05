from load_checking_files import files_exiest, load_budget
from menus import check_user, manager_menu, client_menu, new_line_menu
from auth import user_input, user_loading, authentication
from airlines import play_add_line


def main():
    if files_exiest("credentials.csv") and files_exiest("budget.txt"):
        file_meneger = "credentials.csv"
        file_budget = "budget.csv"
        if check_user() == "menger":
            username, password = user_input()
            user_data = user_loading(file_meneger)
            if authentication(username, password, user_data):
                action_dict = {"1" : "", "2" : play_add_line, "3" : load_budget, "4" : exit}
                user_action = manager_menu()
                action_dict[user_action]()
        else:
            action_dict = {"1" : "", "2" : ""}
            user_action = client_menu()
            # action_dict[user_action]()
    


# # origin_code, dest_code = new()
# test = testing_line_budget(origin_code, dest_code)
# if test:
#     add_line_json(origin_code, dest_code)
    
           
           
main()