from pathlib import Path
import shutil

# Show all folders & files
def show_all():
    base = Path('.')
    for i, item in enumerate(base.rglob("*")):
        print(f"{i+1} : {item}")

# Create folder
def create_folder():
    name = input("Enter folder name: ")
    folder = Path(name)

    if not folder.exists():
        folder.mkdir()
        print(f"Folder '{name}' created successfully.")
    else:
        print(f"Folder '{name}' already exists.")

# Create file inside folder
def create_file_in_folder():
    folder_name = input("Enter folder name: ")
    file_name = input("Enter file name: ")

    folder = Path(folder_name)

    if folder.exists() and folder.is_dir():
        file_path = folder / file_name
        file_path.touch()
        print(f"File '{file_name}' created inside '{folder_name}'")
    else:
        print("Folder does not exist.")

# Rename folder
def rename_folder():
    old_name = input("Enter current folder name: ")
    new_name = input("Enter new folder name: ")

    old_path = Path(old_name)
    new_path = Path(new_name)

    if old_path.exists() and old_path.is_dir():
        old_path.rename(new_path)
        print("Folder renamed successfully.")
    else:
        print("Folder does not exist.")

# Delete folder
def delete_folder():
    name = input("Enter folder name to delete: ")
    folder = Path(name)

    if folder.exists() and folder.is_dir():
        shutil.rmtree(folder)  # delete non-empty folder
        print(f"Folder '{name}' deleted successfully.")
    else:
        print("Folder does not exist.")

# Menu
def menu():
    while True:
        print("\n===== Folder Management System =====")
        print("1. Create Folder")
        print("2. Show All Files/Folders")
        print("3. Create File Inside Folder")
        print("4. Rename Folder")
        print("5. Delete Folder")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            create_folder()
        elif choice == 2:
            show_all()
        elif choice == 3:
            create_file_in_folder()
        elif choice == 4:
            rename_folder()
        elif choice == 5:
            delete_folder()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

# Run program
menu()