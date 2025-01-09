import os

def generate_folder_structure(path, indent=0, ignore_dirs=None):
    """
    Recursively generate the folder and file structure for the given path.

    Args:
        path (str): Path to the folder.
        indent (int): Current level of indentation for the tree structure.
        ignore_dirs (set): Directories to ignore (e.g., '.git').

    Returns:
        str: Formatted folder and file structure.
    """
    if ignore_dirs is None:
        ignore_dirs = {".git"}
    
    output = ""
    items = sorted(os.listdir(path))
    directories = [item for item in items if os.path.isdir(os.path.join(path, item)) and item not in ignore_dirs]
    files = [item for item in items if os.path.isfile(os.path.join(path, item))]
    
    # List directories first
    for item in directories:
        output += "|   " * indent + f"├── {item}/\n"
        output += generate_folder_structure(os.path.join(path, item), indent + 1, ignore_dirs)
    
    # List files
    for item in files:
        output += "|   " * indent + f"├── {item}\n"
    
    return output

if __name__ == "__main__":
    # Determine the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    primary_folder = os.path.basename(script_dir)
    
    # Print the primary folder name
    print(f"{primary_folder}/")
    
    # Generate and print the folder structure
    folder_structure = generate_folder_structure(script_dir)
    print(folder_structure)
