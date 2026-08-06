import os

def menu_break():
    print("=" * 21)

def file_search_menu():
    menu_break()
    print("Please choose a directory to search.")
    menu_break()
    print()

def file_search(user_search):
    menu_break()
    print("File Search")
    menu_break()
    print()

    for current_directory, sub_directories, files in os.walk(user_search):
        print(f"{current_directory}")
        print(f"{sub_directories}")
        print(f"{files}")

while True:
    file_search_menu()
    try:
        user_search = input("Please select a directory.")
        if os.path.isdir(user_search) is True:
            file_search(user_search)
        else:
            print("That directory does not exist.")
    except ValueError:
        print("Please select a directory.")
