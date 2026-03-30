from pathlib import Path

#  Show all files and folders
def readFileandFolder():
    base_path = Path('.')
    items = list(base_path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")

#  Create a new file
def create_file():
    filename = input("Enter the name of the file to create: ")
    file_path = Path(filename)
    if not file_path.exists():
        file_path.touch()
        print(f"File '{filename}' created successfully.")
    else:
        print(f"File '{filename}' already exists.")
    readFileandFolder()

# Update (append text to) a file
def update_file():
    filename = input("Enter the name of the file to update: ")
    file_path = Path(filename)
    if file_path.exists():
        text = input("Enter text to append: ")
        with file_path.open("a") as f:
            f.write(text + "\n")
        print(f"File '{filename}' updated successfully.")
    else:
        print(f"File '{filename}' does not exist.")

#  Read a file
def read_file():
    filename = input("Enter the name of the file to read: ")
    file_path = Path(filename)
    if file_path.exists():
        with file_path.open("r") as f:
            print("File contents:\n")
            print(f.read())
    else:
        print(f"File '{filename}' does not exist.")

#  Delete a file
def delete_file():
    filename = input("Enter the name of the file to delete: ")
    file_path = Path(filename)
    if file_path.exists():
        file_path.unlink()
        print(f"File'{filename}' deleted successfully.")
    else:
        print(f"File'{filename}' does not exist.")

#  Menu
print(" press 1 for creating file")
print(" press 2 for updating file")
print(" press 3 for reading file")
print(" press 4 for delete file")

choice = int(input("Please tell your response :- "))

if choice == 1:
    create_file()
elif choice == 2:
    update_file()
elif choice == 3:
    read_file()
elif choice == 4:
    delete_file()
else:
    print(" Invalid choice ")