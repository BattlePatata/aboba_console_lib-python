import csv, sys, time, os
from colorama import Fore, Style
clear = lambda: os.system("cls")

clear()
print(Style.RESET_ALL + "================= Entering to ====================")
with open("logo.txt", "r", encoding="utf-8") as logo:
    print(Fore.GREEN + Style.BRIGHT +  logo.read() + Style.RESET_ALL)
print("=====" * 10)

user_inpt = input("Do you wish to enter? Y/N: " + Fore.YELLOW).lower()

def quit_foo():
    clear()
    print(Fore.GREEN + "=================== Output =======================")
    print("Have a nice day!")
    print("=====" * 10 + Style.RESET_ALL)
    quit()

def lgn_read():
    with open("login_passw.csv", "r") as log_passw:
        return [{line['id']: {"name": line["name"], "password": line["password"], "favorite": line["favorite"], "admin": line["admin"]}} for line in csv.DictReader(log_passw)]

def lib_read():
    with open("book_lib_dict.csv", "r") as log_passw:
        return [{line['id']: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(log_passw)]

def edit_lib(quit_dict):
    edit_field_names = ["id", "name", "author", "release date"]
    with open("book_lib_dict.csv", "w") as book_lib:
        writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
        writer.writeheader()
        writer.writerows(quit_dict)

def orig_lgn_read():
    with open("login_passw.csv", "r") as log_passw:
        return [{"id": line["id"], "name": line["name"], "password": line["password"], "favorite": line["favorite"], "admin": line["admin"]} for line in csv.DictReader(log_passw)]

def orig_lib_read():
    with open("book_lib_dict.csv", "r") as book_lib:
        return [{"id": line["id"], "name": line["name"], "author": line["author"], "release date": line["release date"]} for line in csv.DictReader(book_lib)]

def main():
    def sign_up_foo():
        user_dict_list = lgn_read()
        
        id_count, field_names = len(user_dict_list) + 1, ["id", "name", "password", "favorite", "admin"]

        print(Style.RESET_ALL + "================== Signing up ====================")
        print(f"This is your id: {id_count}")
        print("-----" * 10)
        print("Please remeber it.")
        print("-----" * 10)
        name_inpt = input("Enter your name: " + Fore.YELLOW + Style.RESET_ALL).title()
        print("-----" * 10)
        print("Your password has to be at least 8 sybols.")
        print("-----" * 10)
        passw_inpt = input("Enter your password: " + Fore.YELLOW + Style.RESET_ALL)
        while len(passw_inpt) < 8:
            print("-----" * 10)
            print("Your password has to be at least 8 sybols!")
            print("-----" * 10)
            passw_inpt = input("Enter your password: "  + Fore.YELLOW + Style.RESET_ALL)
        print("=====" * 10) 
        full_info_dict = {"id": id_count, "name": name_inpt, "password": passw_inpt, "favorite": "0", "admin": "0"}
        
        with open("login_passw.csv", "a") as log_passw:
            writer = csv.DictWriter(log_passw, fieldnames=field_names)
            writer.writerow(full_info_dict)

        sign_in_up_foo()

    def sign_in_foo():
        print(Style.RESET_ALL + "================== Signing in ====================")
        user_inpt = input("Enter your id: " + Fore.YELLOW)
        print(Style.RESET_ALL + "-----" * 10)
        
        def dict_list_to_dict(dict_list):
            cycle, dict = 0, {}

            while cycle < len(dict_list):
                dict.update(dict_list[cycle])
                cycle += 1
            return dict
        
        def user_id_foo():
            return user_inpt
        
        def print_books_foo():
            book_dict_list = lib_read()
            book_dict = dict_list_to_dict(book_dict_list) 
            for key, val in book_dict.items():
                print("-----" * 10)
                print(f"{key}: Book name: {Fore.GREEN + val['name'] + Style.RESET_ALL}, Author: {Fore.GREEN + val['author'] + Style.RESET_ALL}, Year: {Fore.GREEN + val['release date'] + Style.RESET_ALL}")
            print("-----" * 10)
            print("Q: Quit to main menu")
            print("-----" * 10)
            
            return book_dict
        
        def print_users_foo():
            user_dict_list = lgn_read()
            user_dict = dict_list_to_dict(user_dict_list)
            for key, val in user_dict.items():
                print("-----" * 10)
                print(f"{key}: Username: {Fore.GREEN + val['name'] + Style.RESET_ALL}, Password: {Fore.GREEN + val['password'] + Style.RESET_ALL}, Favorite: {Fore.GREEN + val['favorite'] + Style.RESET_ALL}, Admin: {Fore.GREEN + val['admin'] + Style.RESET_ALL}")
            print("-----" * 10)
            print("Q: Quit to main menu")
            print("-----" * 10)
            return user_dict
        
        def admin_opt_print_foo(opt_dict):
            opt_qtty, opt_qtty_inpt = 0, 0
            for key in opt_dict:
                opt_qtty += 1
                print(f"{opt_qtty}: {key.title()}")
            print("Q: Quit")
            print("-----" * 10)
            user_inpt = input("Enter here: " + Fore.YELLOW).lower()

            if user_inpt == "q":
                opt_bool = 0
                admin_option_foo()
                
            for key, foo in opt_dict.items():
                opt_qtty_inpt += 1
                key = ":".join([key, str(opt_qtty_inpt)])
                if user_inpt in key:
                    foo()
            
        def user_opt_print_foo(opt_dict):
            opt_qtty, opt_qtty_inpt = 0, 0
            for key in opt_dict:
                opt_qtty += 1
                print(f"{opt_qtty}: {key.title()}")
            print("Q: Quit")
            print("-----" * 10)
            user_inpt = input("Enter here: " + Fore.YELLOW).lower()

            if user_inpt == "q":
                user_opt_bool = 0
                user_opt_foo()
                
            for key, foo in opt_dict.items():
                opt_qtty_inpt += 1
                key = ":".join([key, str(opt_qtty_inpt)])
                if user_inpt in key:
                    foo()
 
        def load_foo():
            load, item = 0, "~"

            while load < 100:
                load += 10
                item += "~~~~"
                time.sleep(.1)
                clear()
                print(Fore.MAGENTA + f"Loading: {item} {load}%")
            print(Style.RESET_ALL + "-----" * 10)
            print(Fore.GREEN + "Loading complete!")            
        
        user_dict_list, book_dict_list = lgn_read(), lib_read()
        user_dict, book_dict = dict_list_to_dict(user_dict_list), dict_list_to_dict(book_dict_list)

        if user_inpt in user_dict:
            passw_inpt = input("Enter your password: " + Fore.YELLOW)
            clear()
            def name_foo():
                clear()
                print(Style.RESET_ALL + "================== Username ======================")
                print(f"Your username: {Fore.CYAN + user_dict[user_id_foo()]['name'].title()}" + Style.RESET_ALL)      
                print("=====" * 10, "\n")      

            def res_foo(cycle):
                print(f'{cycle}: Name of the book: {Fore.GREEN + book_dict[f"{cycle}"]["name"] + Style.RESET_ALL}, Author: {Fore.GREEN + book_dict[f"{cycle}"]["author"] + Style.RESET_ALL}, Release date: {Fore.GREEN + book_dict[f"{cycle}"]["release date"] + Style.RESET_ALL}') 
                print("-----" * 10)
                      
            def add_srch_favrt_foo(favrt_inpt):
                book_dict_list, check_favrt_list = lib_read(), lgn_read()
                book_dict = dict_list_to_dict(book_dict_list)

                login_field_names = ["id", "name", "password", "favorite", "admin"]
                favrt_field_names = ["id", "name", "author", "release date"]

                if favrt_inpt in book_dict:
                    favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'
                    path = f"./{favrt_file}"
                    check_file = os.path.exists(path)
                    if check_file == True:

                        with open(f"{favrt_file}", "r") as f_name:
                            user_favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(f_name)]    
                            id_count = len(user_favrt_dict_list) + 1
                            full_info_dict = {"id": id_count, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                        
                        with open(f"{favrt_file}", "a") as user_favrt_file:
                            writer = csv.DictWriter(user_favrt_file, fieldnames=favrt_field_names)
                            writer.writerow(full_info_dict)
                    else:
                        full_info_dict = {"id": 1, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                        quit_dict = orig_lgn_read()

                        for info in quit_dict:
                            quit_dict[int(user_id_foo()) - 1]["favorite"] = favrt_file
    
                        with open("login_passw.csv", "w") as log_passw:
                            writer = csv.DictWriter(log_passw, fieldnames=login_field_names)
                            writer.writeheader()
                            writer.writerows(quit_dict)
            
                        with open(f"{favrt_file}", "w") as f_name:
                            writer = csv.DictWriter(f_name, fieldnames=favrt_field_names)
                            writer.writeheader()
                            writer.writerow(full_info_dict)

            if passw_inpt == user_dict[user_inpt]["password"] and user_dict[user_inpt]["admin"] == "1":
                load_foo()
                def edit_name_foo():
                    book_bool = 1         
                    while book_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "============ Editing name of the book ============")
                        print("Which book do you wish to edit?: ")
                        book_dict = print_books_foo()
                        book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()
                        
                        if book_id_inpt in book_dict:
                            print(Style.RESET_ALL + "-----" * 10)
                            edit_inpt, quit_dict = input("Enter new name of the book: " + Fore.YELLOW).title(), orig_lib_read()

                            for info in quit_dict:
                                quit_dict[int(book_id_inpt) - 1]["name"] = edit_inpt
        
                        edit_lib(quit_dict)
                
                        if book_id_inpt == "q":
                            book_bool = 0
                            admin_option_foo()

                def edit_author_foo():
                    book_bool = 1               
                    while book_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "======== Editing author name of the book =========")
                        print("Which book do you wish to edit?: ")
                        book_dict = print_books_foo()
                        book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()
                        
                        if book_id_inpt in book_dict:
                            print(Style.RESET_ALL + "-----" * 10)
                            edit_inpt, quit_dict = input("Enter new author name of the book: " + Fore.YELLOW).title(), orig_lib_read()

                            for info in quit_dict:
                                quit_dict[int(book_id_inpt) - 1]["author"] = edit_inpt
        
                            edit_lib(quit_dict)
                
                        if book_id_inpt == "q":
                            book_bool = 0
                            admin_option_foo()
                
                def edit_year_foo():
                    book_bool = 1    
                    while book_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "============ Editing year of the book ============")
                        book_dict = print_books_foo()
                        book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()

                        if book_id_inpt in book_dict:
                            print(Style.RESET_ALL + "-----" * 10)
                            edit_inpt, quit_dict = input(Style.RESET_ALL + "Enter new release date of the book: " + Fore.YELLOW).title(), orig_lib_read()

                            for info in quit_dict:
                                quit_dict[int(book_id_inpt) - 1]["release date"] = edit_inpt
        
                            edit_lib(quit_dict)
                
                        if book_id_inpt == "q":
                            book_bool = 0
                            admin_option_foo()
                
                def edit_all_foo():
                    book_bool = 1                        
                    while book_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "================ Editing the book ================")
                        print("Which book do you wish to edit?: ")
                        book_dict = print_books_foo()
                        book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()

                        if book_id_inpt in book_dict:
                            book_name_inpt = input(Style.RESET_ALL + "Enter new name of the book: " + Fore.YELLOW).title()
                            print(Style.RESET_ALL + "-----" * 10)
                            book_author_inpt = input("Enter new author name of the book: " + Fore.YELLOW).title()
                            print(Style.RESET_ALL + "-----" * 10)
                            book_year_inpt = input("Enter new release date of the book: " + Fore.YELLOW).title()

                            quit_dict = orig_lib_read()

                            for info in quit_dict:
                                quit_dict[int(book_id_inpt) - 1]["name"] = book_name_inpt
                                quit_dict[int(book_id_inpt) - 1]["author"] = book_author_inpt
                                quit_dict[int(book_id_inpt) - 1]["release date"] = book_year_inpt
        
                            edit_lib(quit_dict)
                
                        if book_id_inpt == "q":
                            book_bool = 0
                            admin_option_foo()

                def edit_opt_foo():
                    clear()
                    edit_opt_dict, edit_opt_bool = {
                        "edit name": edit_name_foo,
                        "edit author": edit_author_foo,
                        "edit year": edit_year_foo,
                        "edit all": edit_all_foo,
                        } ,1
                    
                    while edit_opt_bool == 1:
                        print(Style.RESET_ALL + "================== Edit options ==================")
                        admin_opt_print_foo(edit_opt_dict)
                    
                def del_book_foo():
                    book_bool = 1
                    while book_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "================ Deleting the book ===============")
                        print("Which book do you wish to delete?: ")
                        book_dict = print_books_foo()
                        book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()
                        print(Style.RESET_ALL + "=====" * 10)
                        print()

                        edit_field_names, id_count = ["id", "name", "author", "release date"], 1
                        
                        if book_id_inpt in book_dict:
                            need_del_dict = orig_lib_read()
                            
                            with open("book_lib_dict.csv", "w") as book_lib:
                                writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                writer.writeheader()

                            for info in need_del_dict:

                                if book_id_inpt != info["id"]:
                                    info["id"] = id_count
                                    with open("book_lib_dict.csv", "a") as book_lib:
                                        writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                        writer.writerow(info)
                                    id_count += 1
                                else:
                                    pass
                
                        if book_id_inpt == "q":
                            book_bool = 0
                            admin_option_foo()

                def add_favrt_foo():
                    favrt_bool, check_favrt_list = 1, orig_lgn_read()
                        
                    while favrt_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "============ Adding favorite book ================")
                        print("Which book do you wish to add to your favorites?: ")
                        book_dict = print_books_foo()
                        favrt_inpt = input("Enter here book id: " + Fore.YELLOW).lower()

                        login_field_names = ["id", "name", "password", "favorite", "admin"]
                        favrt_field_names = ["id", "name", "author", "release date"]
                        
                        if favrt_inpt in book_dict:
                            
                            favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'
                            path = f"./{favrt_file}"
                            check_file = os.path.exists(path)

                            if check_file == True:

                                with open(f"{favrt_file}", "r") as f_name:
                                    user_favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(f_name)]    
                                    id_count = len(user_favrt_dict_list) + 1
                                    full_info_dict = {"id": id_count, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                                
                                with open(f"{favrt_file}", "a") as user_favrt_file:
                                    writer = csv.DictWriter(user_favrt_file, fieldnames=favrt_field_names)
                                    writer.writerow(full_info_dict)
                            else:
                                full_info_dict = {"id": 1, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                                
                                quit_dict = orig_lgn_read()

                                for info in quit_dict:
                                    quit_dict[int(user_id_foo()) - 1]["favorite"] = favrt_file
            
                                with open("login_passw.csv", "w") as log_passw:
                                    writer = csv.DictWriter(log_passw, fieldnames=login_field_names)
                                    writer.writeheader()
                                    writer.writerows(quit_dict)

                                with open(f"{favrt_file}", "w") as f_name:
                                    writer = csv.DictWriter(f_name, fieldnames=favrt_field_names)
                                    writer.writeheader()
                                    writer.writerow(full_info_dict)
                
                        if favrt_inpt == "q":
                            favrt_bool = 0
                            admin_option_foo()
                
                def rem_favrt_foo():
                    check_favrt_list = lgn_read()
                    
                    favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'
                    path = f"./{favrt_file}"
                    check_file = os.path.exists(path)
                    
                    if check_file == True:
                        favrt_book_bool = 1
                            
                        while favrt_book_bool == 1:
                            clear()
                            print(Style.RESET_ALL + "================ Deleting the book ===============")
                            print("Which book do you wish to delete?: ")
                            favrt_book_dict = print_books_foo()
                            book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()
                            print(Style.RESET_ALL + "=====" * 10)
                            print()

                            edit_field_names, id_count = ["id", "name", "author", "release date"], 1
                            
                            if book_id_inpt in favrt_book_dict:

                                with open(f"{favrt_file}", "r") as book_lib:
                                    need_del_dict = [{"id": line["id"], "name": line["name"], "author": line["author"], "release date": line["release date"]} for line in csv.DictReader(book_lib)]
                                
                                with open(f"{favrt_file}", "w") as book_lib:
                                    writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                    writer.writeheader()

                                for info in need_del_dict:

                                    if book_id_inpt != info["id"]:
                                        info["id"] = id_count
                                        with open(f"{favrt_file}", "a") as book_lib:
                                            writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                            writer.writerow(info)
                                        id_count += 1
                                    else:
                                        pass
                    
                        if book_id_inpt == "q":
                            favrt_book_bool = 0
                            admin_option_foo()                            
                    else:
                        clear()
                        print(Fore.RED + "==================== Error =======================")
                        print("You don't have favorite books yet.")
                        print("=====" * 10 + Style.RESET_ALL)
                        admin_option_foo()
                
                def search_year_rnge():
                    clear()
                    print(Style.RESET_ALL + "============ Searching by year range =============")
                    low_range_inpt = int(input("Enter starting release year: " + Fore.YELLOW + Style.RESET_ALL))
                    print("-----" * 10)
                    cycle, high_range_inpt = 1, int(input("Enter ending release year: " + Fore.YELLOW + Style.RESET_ALL))
                    clear()
                    print("=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        year_int = int(book_dict[f"{cycle}"]["release date"])
                        if low_range_inpt <= year_int and high_range_inpt >= year_int:
                            res_foo(cycle)
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                
                    if favrt_inpt == "q":
                        admin_option_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)

                def search_name_foo():
                    clear()
                    print(Style.RESET_ALL + "=============== Searching by name ================")
                    user_inpt, cycle = input("Enter name of the book: " + Fore.YELLOW).title() ,1
                    clear()
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        if user_inpt in book_dict[f"{cycle}"]["name"]:
                            res_foo(cycle)
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                    
                    if favrt_inpt == "q":
                        admin_option_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)
                
                def search_year_foo():
                    clear()
                    print(Style.RESET_ALL + "=============== Searching by year ================")
                    user_inpt, cycle = input("Enter release year of the book: " + Fore.YELLOW).title() ,1
                    clear()
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book d8o you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        if user_inpt in book_dict[f"{cycle}"]["release date"]:
                            res_foo(cycle)
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                    
                    if favrt_inpt == "q":
                        admin_option_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)

                def search_author_foo():
                    clear()
                    print(Style.RESET_ALL + "============== Searching by author ===============")
                    user_inpt, cycle = input("Enter author name: " + Fore.YELLOW).title() ,1
                    clear()    
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        if user_inpt in book_dict[f"{cycle}"]["author"]:
                            res_foo(cycle)                
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                    
                    if favrt_inpt == "q":
                        admin_option_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)

                def search_opt_foo():
                    search_dict, search_bool = {
                        "search by name": search_name_foo,
                        "search by year": search_year_foo,
                        "search by author": search_author_foo,
                        "rearch by year range": search_year_rnge,
                        } ,1

                    while search_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "=============== Searching options ================")
                        admin_opt_print_foo(search_dict)

                def add_book_foo():
                    clear()
                    book_dict_list = orig_lib_read()

                    print(Style.RESET_ALL + "================= Adding book! ====================")
                    id_count, field_names = len(book_dict_list) + 1, ["id", "name", "author", "release date"]
                    
                    name_inpt = input("Enter name of the book: " + Fore.YELLOW).title()
                    print(Style.RESET_ALL + "-----" * 10)
                    author_inpt = input(Style.RESET_ALL + "Enter name of the author: " + Fore.YELLOW).title()
                    print(Style.RESET_ALL + "-----" * 10)
                    rele_date = input("Enter release date of the book: " + Fore.YELLOW)

                    full_info_dict = {"id": id_count, "name": name_inpt, "author": author_inpt, "release date": rele_date}
                    with open("book_lib_dict.csv", "a") as book_dict:
                        writer = csv.DictWriter(book_dict, fieldnames=field_names)
                        writer.writerow(full_info_dict)
                    main()

                def favorite_books_foo():
                    check_favrt_list = lgn_read()
                    
                    favrt_count = 0 
                    favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'

                    if check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["favorite"] == "0":
                        print(Style.RESET_ALL + "\n=================== Output =======================")
                        print(f"Dear {Fore.CYAN + check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]['name'].title() + Style.RESET_ALL}, unfortunately you don't have favorite books yet.")
                        print("=====" * 10)
                    else:
                        with open(f"{favrt_file}", "r") as check_favrt_file:
                            favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(check_favrt_file)]
                            
                            print(Style.RESET_ALL + "\n=================== Output =======================")
                            print("Your favorite books:")
                        while favrt_count < len(favrt_dict_list):
                            count = favrt_count + 1
                            id_count = str(count)
                            dict_out = favrt_dict_list[favrt_count][id_count]
                            print("-----" * 10)
                            print(f"Book name: {Fore.GREEN + dict_out['name'] + Style.RESET_ALL}, Author: {Fore.GREEN + dict_out['author'] + Style.RESET_ALL}, Release year: {Fore.GREEN + dict_out['release date'] + Style.RESET_ALL}")
                            favrt_count += 1
                        print("=====" * 10)
                        print()

                    user_inpt = input("Do you wish to continue? Y/N: " + Fore.YELLOW + Style.RESET_ALL).lower()

                    if user_inpt == "n":
                        quit_foo()
                    else:
                        admin_option_foo()
         
                def favrt_opt_foo():
                    clear()
                    favrt_opt_dict, favrt_opt_bool = {
                        "my favorite books": favorite_books_foo,
                        "add favorite book": add_favrt_foo,
                        "delete favorite book": rem_favrt_foo,
                        } ,1
                    
                    while favrt_opt_bool == 1:
                        print(Style.RESET_ALL + "================ Favorite Books ==================")
                        admin_opt_print_foo(favrt_opt_dict)

                def admin_foo():
                    lgn_fild_names, user_bool = ["id", "name", "password", "favorite", "admin"], 1
                        
                    while user_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "================ Editing usernames ===============")
                        print("For which user do you wish to change admin status?: ")
                        user_dict = print_users_foo()
                        id_inpt = input("Enter here user id: " + Fore.YELLOW).lower()
                        
                        if id_inpt == "q":
                            user_bool = 0
                            admin_option_foo()

                        if id_inpt in user_dict:
                            print(Style.RESET_ALL + "-----" * 10)
                            edit_inpt = input("Enter new username: " + Fore.YELLOW).lower()
                            quit_dict = orig_lgn_read()

                            for info in quit_dict:
                                quit_dict[int(id_inpt) - 1]["admin"] = edit_inpt

                            with open("login_passw.csv", "w") as book_lib:
                                writer = csv.DictWriter(book_lib, fieldnames=lgn_fild_names)
                                writer.writeheader()
                                writer.writerows(quit_dict)     

                def edit_usrnames_foo():
                    lgn_fild_names, user_bool = ["id", "name", "password", "favorite", "admin"], 1
                        
                    while user_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "================ Editing usernames ===============")
                        print("Which username do you wish to edit?: ")
                        user_dict = print_users_foo()
                        id_inpt = input("Enter here user id: " + Fore.YELLOW).lower()
                        
                        if id_inpt == "q":
                            user_bool = 0
                            admin_option_foo()

                        if id_inpt in user_dict:
                            print(Style.RESET_ALL + "-----" * 10)
                            edit_inpt = input("Enter new username: " + Fore.YELLOW).lower()                    
                            quit_dict = orig_lgn_read()

                            for info in quit_dict:
                                quit_dict[int(id_inpt) - 1]["name"] = edit_inpt

                            with open("login_passw.csv", "w") as book_lib:
                                writer = csv.DictWriter(book_lib, fieldnames=lgn_fild_names)
                                writer.writeheader()
                                writer.writerows(quit_dict)                 

                def edit_pswrds_foo():
                    lgn_fild_names, user_bool = ["id", "name", "password", "favorite", "admin"], 1
                        
                    while user_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "================ Editing passwords ===============")
                        print("Which username do you wish to edit?: ")
                        user_dict = print_users_foo()
                        id_inpt = input("Enter here user id: " + Fore.YELLOW).lower()
                        
                        if id_inpt == "q":
                            user_bool = 0
                            admin_option_foo()

                        if id_inpt in user_dict:
                            print(Style.RESET_ALL + "-----" * 10)
                            edit_inpt = input("Enter new password: " + Fore.YELLOW)
                    
                            quit_dict = orig_lgn_read()

                            for info in quit_dict:
                                quit_dict[int(id_inpt) - 1]["password"] = edit_inpt

                            with open("login_passw.csv", "w") as book_lib:
                                writer = csv.DictWriter(book_lib, fieldnames=lgn_fild_names)
                                writer.writeheader()
                                writer.writerows(quit_dict)                 

                def edit_users_acc_opt_foo():
                    clear()
                    edit_user_opt_dict, edit_user_opt_bool = {
                        "give admin status": admin_foo,
                        "edit usernames": edit_usrnames_foo,
                        "edit passwords": edit_pswrds_foo,
                        } ,1
                    
                    while edit_user_opt_bool == 1:
                        print(Style.RESET_ALL + "================ Account editor ==================")
                        admin_opt_print_foo(edit_user_opt_dict)

                def admin_option_foo():
                    opt_dict, opt_bool = {
                        "edit user accounts": edit_users_acc_opt_foo,
                        "see username": name_foo,
                        "add book": add_book_foo,
                        "edit book": edit_opt_foo,
                        "delete book": del_book_foo,
                        "search": search_opt_foo,
                        "favorite books": favrt_opt_foo,
                        } ,1
                    
                    while opt_bool == 1:
                        opt_qtty, opt_qtty_inpt = 0, 0
                        print(Style.RESET_ALL + "=============  Welcome to Library! ===============")
                        for key in opt_dict:
                            opt_qtty += 1
                            print(f"{opt_qtty}: {key.title()}")
                        print("Q: Quit")
                        print("-----" * 10)
                        user_inpt = input("Enter here: " + Fore.YELLOW).lower()

                        if user_inpt == "q":
                            opt_bool = 0
                            sign_in_up_foo()
                            
                        for key, foo in opt_dict.items():
                            opt_qtty_inpt += 1
                            key = ":".join([key, str(opt_qtty_inpt)])
                            if user_inpt in key:
                                foo()
                admin_option_foo()
            elif passw_inpt == user_dict[user_inpt]["password"] and user_dict[user_inpt]["admin"] == "0":
                load_foo()
                def add_favrt_foo():
                    favrt_bool, check_favrt_list = 1, orig_lgn_read()
                        
                    while favrt_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "============ Adding favorite book ================")
                        print("Which book do you wish to add to your favorites?: ")
                        book_dict = print_books_foo()
                        favrt_inpt = input("Enter here book id: " + Fore.YELLOW).lower()

                        login_field_names = ["id", "name", "password", "favorite", "admin"]
                        favrt_field_names = ["id", "name", "author", "release date"]
                        
                        if favrt_inpt in book_dict:
                            
                            favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'
                            path = f"./{favrt_file}"
                            check_file = os.path.exists(path)

                            if check_file == True:

                                with open(f"{favrt_file}", "r") as f_name:
                                    user_favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(f_name)]    
                                    id_count = len(user_favrt_dict_list) + 1
                                    full_info_dict = {"id": id_count, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                                
                                with open(f"{favrt_file}", "a") as user_favrt_file:
                                    writer = csv.DictWriter(user_favrt_file, fieldnames=favrt_field_names)
                                    writer.writerow(full_info_dict)
                            else:
                                full_info_dict = {"id": 1, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                                
                                quit_dict = orig_lgn_read()

                                for info in quit_dict:
                                    quit_dict[int(user_id_foo()) - 1]["favorite"] = favrt_file
            
                                with open("login_passw.csv", "w") as log_passw:
                                    writer = csv.DictWriter(log_passw, fieldnames=login_field_names)
                                    writer.writeheader()
                                    writer.writerows(quit_dict)

                                with open(f"{favrt_file}", "w") as f_name:
                                    writer = csv.DictWriter(f_name, fieldnames=favrt_field_names)
                                    writer.writeheader()
                                    writer.writerow(full_info_dict)
                
                        if favrt_inpt == "q":
                            favrt_bool = 0
                            user_opt_foo()
                
                def rem_favrt_foo():
                    check_favrt_list = lgn_read()
                    
                    favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'
                    path = f"./{favrt_file}"
                    check_file = os.path.exists(path)
                    
                    if check_file == True:
                        favrt_book_bool = 1
                            
                        while favrt_book_bool == 1:
                            clear()
                            print(Style.RESET_ALL + "================ Deleting the book ===============")
                            print("Which book do you wish to delete?: ")
                            favrt_book_dict = print_books_foo()
                            book_id_inpt = input("Enter here book id: " + Fore.YELLOW).lower()
                            print(Style.RESET_ALL + "=====" * 10)
                            print()

                            edit_field_names, id_count = ["id", "name", "author", "release date"], 1
                            
                            if book_id_inpt in favrt_book_dict:

                                with open(f"{favrt_file}", "r") as book_lib:
                                    need_del_dict = [{"id": line["id"], "name": line["name"], "author": line["author"], "release date": line["release date"]} for line in csv.DictReader(book_lib)]
                                
                                with open(f"{favrt_file}", "w") as book_lib:
                                    writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                    writer.writeheader()

                                for info in need_del_dict:

                                    if book_id_inpt != info["id"]:
                                        info["id"] = id_count
                                        with open(f"{favrt_file}", "a") as book_lib:
                                            writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                            writer.writerow(info)
                                        id_count += 1
                                    else:
                                        pass
                    
                        if book_id_inpt == "q":
                            favrt_book_bool = 0
                            admin_option_foo()                            
                    else:
                        clear()
                        print(Fore.RED + "==================== Error =======================")
                        print("You don't have favorite books yet.")
                        print("=====" * 10 + Style.RESET_ALL)
                        user_opt_foo()

                def search_year_rnge():
                    clear()
                    print(Style.RESET_ALL + "============ Searching by year range =============")
                    low_range_inpt = int(input("Enter starting release year: " + Fore.YELLOW))
                    print(Style.RESET_ALL + "-----" * 10)
                    cycle, high_range_inpt = 1, int(input("Enter ending release year: " + Fore.YELLOW))
                    clear()
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        year_int = int(book_dict[f"{cycle}"]["release date"])
                        if low_range_inpt <= year_int and high_range_inpt >= year_int:
                            res_foo(cycle)
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                
                    if favrt_inpt == "q":
                        user_opt_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)

                def search_name_foo():
                    clear()
                    print(Style.RESET_ALL + "=============== Searching by name ================")
                    user_inpt, cycle = input("Enter name of the book: " + Fore.YELLOW).title() ,1
                    clear()
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        if user_inpt in book_dict[f"{cycle}"]["name"]:
                            res_foo(cycle)
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                    
                    if favrt_inpt == "q":
                        user_opt_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)
                
                def search_year_foo():
                    clear()
                    print(Style.RESET_ALL + "=============== Searching by year ================")
                    user_inpt, cycle = input("Enter release year of the book: " + Fore.YELLOW).title() ,1
                    clear()
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        if user_inpt in book_dict[f"{cycle}"]["release date"]:
                            res_foo(cycle)
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                    
                    if favrt_inpt == "q":
                        user_opt_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)

                def search_author_foo():
                    clear()
                    print(Style.RESET_ALL + "============== Searching by author ===============")
                    user_inpt, cycle = input("Enter author name: " + Fore.YELLOW).title() ,1
                    clear()    
                    print(Style.RESET_ALL + "=================== Output =======================")
                    print("Which book do you wish to add to your favorites?")
                    while cycle < len(book_dict) + 1:
                        if user_inpt in book_dict[f"{cycle}"]["author"]:
                            res_foo(cycle)                
                        cycle += 1
                    print("Q: Quit to main menu")
                    print("-----" * 10)
                    favrt_inpt = input("Enter book ID: " + Fore.YELLOW).lower()
                    
                    if favrt_inpt == "q":
                        user_opt_foo()
                    else:
                        add_srch_favrt_foo(favrt_inpt)

                def search_opt_foo():
                    search_dict, search_bool = {
                        "search by name": search_name_foo,
                        "search by year": search_year_foo,
                        "search by author": search_author_foo,
                        "rearch by year range": search_year_rnge,
                        } ,1

                    while search_bool == 1:
                        clear()
                        print(Style.RESET_ALL + "=============== Searching options ================")
                        user_opt_print_foo(search_dict)

                def favorite_books_foo():
                    check_favrt_list = lgn_read()
                    
                    favrt_count = 0 
                    favrt_file = f'{check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["name"]}_favrt.csv'

                    if check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]["favorite"] == "0":
                        print(Style.RESET_ALL + "\n=================== Output =======================")
                        print(f"Dear {Fore.CYAN + check_favrt_list[int(user_id_foo()) - 1][user_id_foo()]['name'].title() + Style.RESET_ALL}, unfortunately you don't have favorite books yet.")
                        print("=====" * 10)
                    else:
                        with open(f"{favrt_file}", "r") as check_favrt_file:
                            favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(check_favrt_file)]
                            
                            print(Style.RESET_ALL + "\n=================== Output =======================")
                            print("Your favorite books:")
                        while favrt_count < len(favrt_dict_list):
                            count = favrt_count + 1
                            id_count = str(count)
                            dict_out = favrt_dict_list[favrt_count][id_count]
                            print("-----" * 10)
                            print(f"Book name: {Fore.GREEN + dict_out['name'] + Style.RESET_ALL}, Author: {Fore.GREEN + dict_out['author'] + Style.RESET_ALL}, Release year: {Fore.GREEN + dict_out['release date'] + Style.RESET_ALL}")
                            favrt_count += 1
                        print("=====" * 10)
                        print()

                    user_inpt = input("Do you wish to continue? Y/N: " + Fore.YELLOW + Style.RESET_ALL).lower()

                    if user_inpt == "n":
                        quit_foo()
                    else:
                        user_opt_foo()

                def favrt_opt_foo():
                    clear()
                    favrt_opt_dict, favrt_opt_bool = {
                        "my favorite books": favorite_books_foo,
                        "add favorite book": add_favrt_foo,
                        "delete favorite book": rem_favrt_foo,
                        } ,1
                    
                    while favrt_opt_bool == 1:
                        print(Style.RESET_ALL + "================ Favorite Books ==================")
                        user_opt_print_foo(favrt_opt_dict)

                def edit_username_foo():
                    lgn_fild_names = ["id", "name", "password", "favorite", "admin"]

                    print(Style.RESET_ALL + "================ Editing username ================")
                    usrname_inpt, quit_dict = input("Enter your new username: ").lower(), orig_lgn_read()
                    
                    for info in quit_dict:
                        quit_dict[int(user_id_foo()) - 1]["name"] = usrname_inpt

                    with open("book_lib_dict.csv", "w") as book_lib:
                        writer = csv.DictWriter(book_lib, fieldnames=lgn_fild_names)
                        writer.writeheader()
                        writer.writerows(quit_dict)

                def edit_passw_foo():
                    lgn_fild_names = ["id", "name", "password", "favorite", "admin"]

                    print(Style.RESET_ALL + "================ Editing password ================")
                    pswrd_inpt, quit_dict = input("Enter your new password: "), orig_lgn_read()

                    for info in quit_dict:
                        quit_dict[int(user_id_foo()) - 1]["password"] = pswrd_inpt

                    with open("book_lib_dict.csv", "w") as book_lib:
                        writer = csv.DictWriter(book_lib, fieldnames=lgn_fild_names)
                        writer.writeheader()
                        writer.writerows(quit_dict)                       

                def edit_user_acc_opt_foo():
                    clear()
                    edit_user_opt_dict, edit_user_opt_bool = {
                        "edit username": edit_username_foo,
                        "edit password": edit_passw_foo,
                        } ,1
                    
                    while edit_user_opt_bool == 1:
                        print(Style.RESET_ALL + "================ Account editor ==================")
                        user_opt_print_foo(edit_user_opt_dict)

                def user_opt_foo():
                    user_opt_dict, user_opt_bool = {
                        "edit account": edit_user_acc_opt_foo,
                        "see username": name_foo,
                        "search": search_opt_foo,
                        "your favorite books": favrt_opt_foo,
                        } ,1
                    
                    while user_opt_bool == 1:
                        opt_qtty, opt_qtty_inpt = 0, 0
                        print(Style.RESET_ALL + "=============  Welcome to Library! ===============")
                        for key in user_opt_dict:
                            opt_qtty += 1
                            print(f"{opt_qtty}: {key.title()}")
                        print("Q: Quit")
                        print("-----" * 10)
                        user_inpt = input("Enter here: " + Fore.YELLOW).lower()

                        if user_inpt == "q":
                            user_opt_bool = 0
                            sign_in_up_foo()
                            
                        for key, foo in user_opt_dict.items():
                            opt_qtty_inpt += 1
                            key = ":".join([key, str(opt_qtty_inpt)])
                            if user_inpt in key:
                                foo()
                user_opt_foo()
            else:
                clear()
                print(Fore.RED + "==================== Error =======================")
                print("Wrong password!")
                print("=====" * 10 + Style.RESET_ALL)
                user_inpt = input("Press enter to try again: " + Fore.YELLOW)
                sign_in_foo()
        else:
            clear()
            print(Fore.RED + "==================== Error =======================")
            print("This id doesn't exist.")
            print("=====" * 10)
            user_inpt = input(Style.RESET_ALL + "Press enter to try again: " + Fore.YELLOW)
            sign_in_up_foo()

    def sign_in_up_foo():
        enter_dict, sign_bool = {
            "1: sign up": sign_up_foo,
            "2: sign in": sign_in_foo,
            }, 1
        
        while sign_bool == 1:
            clear()
            print(Style.RESET_ALL + "============  Welcome to Aboba shop! =============")
            for key in enter_dict:
                print(f"{key.split(':')[0]}:{key.split(':')[1].title()}")
            print("Q: Quit")
            print("-----" * 10)
            cust_input = input("Enter here: " + Fore.YELLOW).lower()

            if cust_input == "q":
                sign_bool = 0
                quit_foo()

            for key, foo in enter_dict.items():
                if cust_input in key:    
                    foo()
    sign_in_up_foo()

if user_inpt == "y":
    main()
else:
    quit_foo()