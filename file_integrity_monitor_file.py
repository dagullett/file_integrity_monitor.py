import os
import hashlib
import json


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

    # Stores the hashes from the CURRENT scan
    hash_stored_file = {}

    # Location of the OLD baseline
    json_hash_stores = "C:\\Users\\default_user\\Desktop\\json_stores\\json_hash_stores.json"

    # Load the OLD baseline once
    with open(json_hash_stores, "r") as json_file:
        old_hashes = json.load(json_file)

    # Scan the directory
    for current_directory, _, files in os.walk(user_search):

        # Leaving these in for debugging future issues.
        # print(f"{current_directory}")
        # print(f"{files}")

        hashed_files(
            current_directory,
            files,
            hash_stored_file,
            old_hashes
        )

    # The current scan is now complete, so check for deleted files
    file_delete_hash(old_hashes, hash_stored_file)


def hashed_files(current_directory, files, hash_stored_file, old_hashes):

    for file in files:
        file_path = os.path.join(current_directory, file)

        print(file_path)

        with open(file_path, "rb") as file_document:
            file_document_contents = file_document.read()

            file_hash = hashlib.sha256(file_document_contents)

        print(file_hash.hexdigest())

        # Add this file to the CURRENT scan dictionary
        hash_stored_file[file_path] = file_hash.hexdigest()

        # Check whether the file is new or modified
        file_hash_comparison(
            old_hashes,
            file_path,
            file_hash
        )


def file_hash_comparison(old_hashes, file_path, file_hash):

    # File existed in the old baseline
    if file_path in old_hashes:

        # File exists, but its contents changed
        if file_hash.hexdigest() != old_hashes[file_path]:
            print("This file was modified.")

    # File doesn't exist in the old baseline
    else:
        print("This is a new file.")


def file_delete_hash(old_hashes, hash_stored_file):

    # Creates old_file_path from each path stored in old_hashes
    for old_file_path in old_hashes:

        # Old file is missing from the current scan
        if old_file_path not in hash_stored_file:
            print(f"This file was deleted: {old_file_path}")


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
