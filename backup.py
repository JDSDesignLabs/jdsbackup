from pathlib import Path
import shutil as backup
from tkinter import *
from tkinter import ttk, filedialog

class BackupSystem:
    def __init__(self, root):
            root.title("JDS Backup")
            # create proper padding for grid
            mainframe = ttk.Frame(root, padding="3 3 12 12")
            mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
            root.columnconfigure(0, weight=1)
            root.rowconfigure(0, weight=1)
            
            # First text box for source file entry
            backup_src = StringVar()
            backup_src_entry = ttk.Label(mainframe, width=7, textvariable=backup_src)
            backup_src_entry.grid(column=3, row=1, sticky=(W,E))

            # Second text box for source file entry
            backup_dst = StringVar()
            ttk.Label(mainframe, textvariable=backup_dst).grid(column=3, row=2, sticky=(W,E))

            # Shows the provided file location given exists
            backup_complete=StringVar()
            ttk.Label(mainframe, textvariable=backup_complete).grid(column=1, row=4, sticky=(W,E))
            
            

            # Shows source label
            ttk.Label(mainframe, text="Source: ").grid(column=1, row=1, sticky=W)
            ttk.Label(mainframe, text="Destination: ").grid(column=1, row=2, sticky=W)
            
            # Create buttons
            filename = ttk.Button(mainframe, text="Select Source", command=lambda: select_file()).grid(column=4, row=1, sticky=W)
            ttk.Button(mainframe, text="Select Destination", command=lambda: select_directory(filename)).grid(column=4, row=2, sticky=W)
            ttk.Button(mainframe, text="Backup", command=lambda: perform_backup(backup_src.get(), backup_dst.get(), backup_type = 'n')).grid(column=1, row=3, sticky=W)
            ttk.Button(mainframe, text="Scheduled Backup", command=lambda: perform_backup(backup_src.get(), backup_dst.get(), backup_type = 's')).grid(column=3, row=3, sticky=W)
            ttk.Button(mainframe, text="Incremental Backup", command=lambda: perform_backup(backup_src.get(), backup_dst.get(), backup_type = 'i')).grid(column=4, row=3, sticky=W)

            
            for child in mainframe.winfo_children():
                child.grid_configure(padx=5, pady=5)
            backup_src_entry.focus()
            root.bind("<Return>", backup)

            def select_file():
                filename = filedialog.askopenfilename()
                backup_src.set(filename)

            def select_directory(filename):
                directoryname = filedialog.askdirectory()
                filename = str(backup_src.get()) +'.backup'
                filename = filename.split('/')
                backup_dst.set(directoryname + "/" + filename[len(filename) - 1])
                 

            # Backup Logic
            def perform_backup(src, dst, backup_type):
                print("Backup in progress...")
            # handle the error returned if specified file is not found    
                if backup_type == 'n':
                    try:
                        backup.copyfile(src, dst)
                        backup_complete.set("Backup Complete.")
                    except FileNotFoundError:
                        backup_complete.set("File Not Found.")     
                elif backup_type == 's':
                    print("Scheduled backup")
                elif backup_type == 'i':
                    print("incremental backup")

def main():
    # set up the window
    root=Tk()
    BackupSystem(root)
    root.mainloop()

if __name__ == '__main__':
    main()