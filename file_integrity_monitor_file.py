import os
import hashlib

def menu_break():
    print("=" * 21)

def file_search_menu():
    menu_break()
    print("Directory File Search")
    menu_break()
    print()

def file_search(user_search):
    menu_break()
    print("Searching Files...")
    menu_break()
    print()

    for current_directory, sub_directories, files in os.walk(user_search):
    # Leaving these in for debugging future issues.
       # print(f"{current_directory}")
       # print(f"{sub_directories}")
       # print(f"{files}")

        for file in files:
            file_path = os.path.join(current_directory, file)
            print(file_path)
            with open(file_path, "rb") as file_document:
                file_document_contents = file_document.read()
                file_hash = hashlib.sha256(file_document_contents)
                print(file_hash.hexdigest())
                
while True:
    file_search_menu()
    try:
        user_search = input("Please select a directory to search: ")
        if os.path.isdir(user_search) is True:
            file_search(user_search)
        else:
            print("That directory does not exist.")
    except ValueError:
        print("Please choose a directory to search: ")
