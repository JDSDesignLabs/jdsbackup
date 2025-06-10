from pathlib import Path
import shutil as backup
from tkinter import *
from tkinter import ttk



def menu():
    option_provided = False
    menu_items = ['Exit', 'Standard Backup', 'Backup/Compress', ]
    print("JDS Designs - Backup Script v1")

    i = 0
    for item in menu_items:
        print(f'{i}. {item}')
        i+=1
    
    while not option_provided:
        try:
            user_selection = input("Please select an option: ")
            if user_selection == '1':
                return '1'
            if user_selection == '2':
                return '2'
            if user_selection == '0':
                return '0'
        except ValueError:
            print("Please enter a value")

# Backup Logic
def standard_backup(src, dst):
    print("Backup in progress...")
# handle the error returned if specified file is not found    
    try:
        backup.copyfile(src, dst)
        print("Backup Succcessful")
    except FileNotFoundError:
        print("File not found")



def get_source():
    valid_path = False
    while not valid_path:
    #  ask user for file they would like to back up and store in variable a
        a = input("Please enter the location of the file you would like to back up: ")
        # convert to path object to be checked by Path
        path = Path(a)
        # determine if it is file
        if path.is_file():
            is_right_file = 0
            while is_right_file == 0:
                # Ask user to confirm backup to validate it is the correct file
                user_selection = input(f"Please confirm if you would like to backup file:  {path}  (Y/N):")
                # if the user confirms its the correct file
                    # assign flag to 1
                if user_selection == "Y":
                    is_right_file = 1
                    valid_path = True
                    # else print please retry and loop
                else:
                    user_selection = input("Would you like to (R)etry or (E)xit to main menu?(R/E): ")
                    if user_selection == 'E':
                        return()

        else:
                # displays to user that file provided was incorrect
            print("Invalid file") 

    return(path)   

def get_dst(src):
    dst =  str(src) + '.backup'
    # split given source file location by \ delimiter
    file_name_split = dst.split("\\")
    # get filename
    file_name = file_name_split[len(file_name_split) - 1]
    print(f"Current backup location: {dst}")
    user_selection = input("Would you like to set a custom backup location?(Y/N): ")
    if user_selection == 'Y':
        valid_path = False
        while not valid_path:
        #  ask user for file location they would like to back up to and store in variable a
            a = input("Please enter the location you would like to back up to: ")
            # convert to path object to be checked by Path methods
            path = Path(a)
            # determine if it is a legit directory
            if path.is_dir():
                is_right_file = 0
                while is_right_file == 0:
                    # Ask user to confirm backup to validate it is the correct file
                    user_selection = input(f"Please confirm if the following backup location / filename is correct:  {str(path)}\{file_name}  (Y/N):")
                    # if the user confirms its the correct file
                        # assign flag to 1
                    if user_selection == "Y":
                        is_right_file = 1
                        valid_path = True
                        return(str(path) +"\\" + str(file_name))
                    # else print please retry and loop
                    else:
                        user_selection = input("Would you like to (R)etry or (E)xit to main menu?(R/E): ")
                        if user_selection == 'E':
                            return()
        else:
            # displays to user that file provided was incorrect
            print("Invalid file")
            return(path) 

    elif user_selection == 'N':
        return dst

## Backup data logic -- this is the logic that will ask the user for input prior to calling the backup function and sending the required file path
def standard_backup_setup():
    src = get_source()
    dst = get_dst(src)
    standard_backup(src, dst)

## implement compression backup - in progress
def compress_backup():
    print("You chose to backup and compress")



def main():
    # execute code via terminal window to test
    running = True
    while running:
        user_selection = menu()
        match  int(user_selection):
            case 1:
                standard_backup_setup()
            case 2:
                compress_backup()
            case 0:
                print("Exiting System")
                running = False
                exit()    

if __name__ == '__main__':
    main()