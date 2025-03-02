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

    # Iterate over the directory content
    for item in os.listdir(directory):
        if item in IGNORE:
            item_path = os.path.join(directory, item)
            
            # If it's a directory in the ignore list, include it but skip its subdirectories and files
            if os.path.isdir(item_path):
                structure[item] = None  # Only include the directory name, but no subfiles
            else:
                continue  # Skip the file itself if it's in the ignore list
        else:
            item_path = os.path.join(directory, item)
            
            # If it's a directory, recurse into it
            if os.path.isdir(item_path):
                structure[item] = get_directory_structure(item_path, include_files)
            elif include_files:
                structure[item] = None  # If it's a file and include_files is True, add the file

    return structure

# Function to format the directory structure
def format_structure(structure, level=0):
    result = ""
    for item, substructure in structure.items():
        # Add "/" only for directories
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

        # Get the directory structure
        structure = get_directory_structure(directory, include_files)
        
        # Print the formatted directory structure
        print(format_structure(structure))

