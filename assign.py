# Ask the user for a filename and handle errors if it doesn't exist or can't be read

filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: Permission denied for '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")# Create and fill the input file with some text