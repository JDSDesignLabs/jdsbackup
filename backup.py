from pathlib import Path
import shutil as backup
from tkinter import *
from tkinter import ttk 

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
            backup_src_entry = ttk.Entry(mainframe, width=7, textvariable=backup_src)
            backup_src_entry.grid(column=3, row=1, sticky=(W,E))

            # Second text box for source file entry
            backup_dst = StringVar()
            backup_dst_entry = ttk.Entry(mainframe, width=7, textvariable=backup_dst)
            backup_dst_entry.grid(column=3, row=2, sticky=(W,E))

            # Shows the provided file location given exists
            backup_complete=StringVar()
            ttk.Label(mainframe, textvariable=backup_complete).grid(column=4, row=1, sticky=(W,E))
            
            # Shows source label
            ttk.Label(mainframe, text="Source: ").grid(column=1, row=1, sticky=W)
            ttk.Label(mainframe, text="Destination: ").grid(column=1, row=2, sticky=W)
            
            ttk.Button(mainframe, text="Backup", command=lambda: standard_backup(backup_src.get(), backup_dst.get())).grid(column=3, row=3, sticky=W)

            
            for child in mainframe.winfo_children():
                child.grid_configure(padx=5, pady=5)
            backup_src_entry.focus()
            root.bind("<Return>", backup)

            # Backup Logic
            def standard_backup(src, dst):
                print("Backup in progress...")
            # handle the error returned if specified file is not found    
                try:
                    backup.copyfile(src, dst)
                    backup_complete.set("Backup Complete.")
                except FileNotFoundError:
                    backup_complete.set("File Not Found.")     

def main():
    # set up the window
    root=Tk()
    BackupSystem(root)
    root.mainloop() 

if __name__ == '__main__':
    main()