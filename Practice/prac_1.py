"""Program to demonstrate the use of File Handling in Python"""
print("="*50)
print("File Handling in Python")
print("="*50)
def create_file():
    # Create a new file and write some content to it
    global file_name
    file_name = input("Enter the name of the file to create (with .txt extension): ")
    with open(file_name,"w") as file:
        file.write("This is a sample text file.\n")
        file.write("It contains some sample text.\n")
        file.write("File handling is an important concept in Python.\n")
        print("File created successfully!")

def read_file():
    # Read the content of the file and display it
    global file_name
    with open(file_name,"r") as file:
        content = file.read()
        print("Content of the file:")
        print(content)

def append_file():
    # Append some content to the existing file
    global file_name
    with open(file_name,"a") as file:
        details = input("Enter the content to append to the file: ")
        file.write(details + "\n")
        print("Content appended successfully!")        

def delete_file():
    # Delete the file
    import os
    global file_name
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File deleted successfully!")
    else:
        print("The file does not exist.")

def read_file_line_by_line():
    # Read the content of the file line by line and display it
    global file_name
    with open(file_name,"r") as file:
        print("Content of the file (line by line):")
        for line in file:
            print(line.strip())        

def main():
    while True:
        print("\nMenu:")
        print("1. Create a new file")
        print("2. Read the content of the file")
        print("3. Append content to the file")
        print("4. Delete the file")
        print("5. Read the content of the file line by line")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            append_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            read_file_line_by_line()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

    
    