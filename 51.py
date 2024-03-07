#Ex1
import os
def list_dir_files(path):
    print("Directories:")
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            print(name)
            
            print("\nFiles:")
            for name in os.listdir(path):
                if os.path.isfile(os.path.join(path, name)):
                    print(name)

    print("\nAll directories and files:")
    for name in os.listdir(path):
        print(name)

#Ex2
        import os

def check_path_access(path):
    exists = os.path.exists(path)
    print(f"Path exists: {exists}")

    if exists:
        readable = os.access(path, os.R_OK)
        print(f"Path is readable: {readable}")
    else:
        print("Path is not readable: path does not exist")

    if exists:
        writable = os.access(path, os.W_OK)
        print(f"Path is writable: {writable}")
    else:
        print("Path is not writable: path does not exist")

    if exists:
        executable = os.access(path, os.X_OK)
        print(f"Path is executable: {executable}")
    else:
        print("Path is not executable: path does not exist")

#Ex3
        import os

def test_path(path):
   
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
    
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")
                                   
#Ex 4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)


file_path = 'some.txt'

try:
    line_count = count_lines(file_path)
    print(f"The file '{file_path}' has {line_count} lines.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

#Ex5
def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write("%s\n" % item)

file_path = 'some.txt'
data_list = ['kbtu', 'sdu', 'kimep', 'aitu']

try:
    write_list_to_file(file_path, data_list)
    print(f"The list has been written to the file '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
#Ex6
import string
import os

file_names = [f"{char}.txt" for char in string.ascii_uppercase]

for file_name in file_names:
    with open(file_name, 'w') as file:
        file.write(f"This is file {file_name}\n")

print("Files A.txt through Z.txt have been created.")     
#Ex7
def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            contents = source.read()
            destination.write(contents)
        print(f"Contents of '{source_file}' have been successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"The file '{source_file}' was not found.")

source_file_path = 'some.txt'
destination_file_path = 'destination.txt'

copy_file_contents(source_file_path, destination_file_path)
#Ex8
import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.R_OK):
            try:
                os.remove(file_path)
                print(f"The file '{file_path}' has been deleted.")
            except Exception as e:
                print(f"An error occurred while deleting the file: {e}")
        else:
            print(f"The file '{file_path}' is not accessible for reading.")
    else:
        print(f"The file '{file_path}' does not exist.")

file_path_to_delete = 'some.txt'
delete_file(file_path_to_delete)   

 

    
      