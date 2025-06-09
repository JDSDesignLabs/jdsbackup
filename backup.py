import os
from pathlib import Path
import shutil as backup


def menu():
    menu_items = ['Standard Backup', 'Backup/Compress', ]
    print(len(menu_items))
    print("JDS Designs - Backup Script v1")

    i = 1
    for item in menu_items:    
        print(f'{i}. {item}')
        i+=1
    user_selection = input("Please select an option: ")

    if user_selection == '1':
        return '1'

    if user_selection == '2':
        return '2'

# Backup Logic
def standard_backup(src, dst):
    print("Packup in progress...")
    backup.copyfile(src, dst)

    

## Backup data logic -- this is the logic that will ask the user for input prior to calling the backup function and sending the required file path
def standard_backup_setup():
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
            # else print please retry and loop
            else:
                user_selection = input("Would you like to (R)etry or (E)xit?(R/E): ")
                if user_selection == 'E':
                    return()

    else:
        # displays to user that file provided was incorrect
        print("Invalid file")

    standard_backup(path, dst = 0)


## implement compression backup
def compress_backup():
    print("You chose to backup and compress")



def main():
    user_selection = menu()
    match  int(user_selection):
        case 1:
            standard_backup_setup()
        case 2:
            compress_backup()


if __name__ == '__main__':
    main()