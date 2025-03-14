import os

# Function to load the list of files and folders to be ignored
def load_ignore_list(filename="ignore"):
    try:
        # Get the directory where the script is located (the script's folder)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)  
        with open(file_path, 'r') as f:
            # Returns a set of items to ignore, removing extra spaces and empty lines
            return {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Warning: {filename} not found at {file_path}. No items will be ignored.")
        return set()

# Function to get the directory structure
def get_directory_structure(directory, include_files=True):
    structure = {}
    
    # Check if the directory exists
    if not os.path.exists(directory):
        return f"The directory {directory} does not exist."
    
    # Load the ignore list
    IGNORE = load_ignore_list()

    # Separate folders and files for sorting
    folders = []
    files = []
    
    for item in os.listdir(directory):
        if item in IGNORE:
            continue  # Skip ignored items
        
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            folders.append(item)
        elif include_files:
            files.append(item)
    
    # Sort folders and files alphabetically
    folders.sort()
    files.sort()
    
    for folder in folders:
        structure[folder] = get_directory_structure(os.path.join(directory, folder), include_files)
    
    for file in files:
        structure[file] = None
    
    return structure

# Function to format the directory structure
def format_structure(structure, level=0):
    result = ""
    for item, substructure in structure.items():
        if isinstance(substructure, dict):  # If it's a subfolder
            result += "    " * level + f"{item}/\n"  # Append "/" to directories
            result += format_structure(substructure, level + 1)
        else:  # If it's a file
            result += "    " * level + f"{item}\n"
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path> [-p | -a]")
    else:
        directory = sys.argv[1]  # Capture the provided directory
        
        # Check if the option to include only folders (-p) was passed
        include_files = True
        if len(sys.argv) == 3:
            if sys.argv[2] == '-p':
                include_files = False
            elif sys.argv[2] != '-a':
                print("Invalid option. Use '-p' for folders only or '-a' for files and folders.")
                sys.exit(1)

        structure = get_directory_structure(directory, include_files)
        
        print(format_structure(structure))

