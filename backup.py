import os


def menu():
    menu_items = ['Standard Backup', 'Backup/Compress', ]
    print(len(menu_items))
    print("JDS Designs - Backup Script v1")

    i = 1
    for item in menu_items:    
        print(f'{i}. {item}')
        i+=1
    user_selection = input("Please select an option: ")

    if user_selection is '1':
        return '1'

    if user_selection is '2':
        return '2'

## Implement standard backup function
def standard_backup():
    a = input("Please enter the location of the file you would like to back up: ")
    print(a)


## implement compression backup
def compress_backup():
    print("You chose to backup and compress")



def main():
    user_selection = menu()
    match  int(user_selection):
        case 1:
            standard_backup()
        case 2:
            compress_backup()


if __name__ == '__main__':
    main()