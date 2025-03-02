
# Directory Tree Script

This script generates a directory tree structure for a given directory, including an option to specify which files and folders should be ignored based on a configuration file.

## Features

- Generates a directory tree structure for a given path.
- Includes an option to list only folders or both files and folders.
- Uses an `ignore` file to exclude specific files and folders from the directory structure.
- Prints directories with a trailing slash (`/`) to clearly differentiate them from files.
- Supports recursive exploration of subdirectories.
- The script works for any directory on your filesystem.

## Requirements

- Python 3.x

## Setup

1. Clone or download the repository.
2. Ensure you have Python 3 installed.

## Usage

To run the script, use the following command:

```bash
python script.py <directory_path> [-p | -a]
```

### Arguments:
- `<directory_path>`: The path to the directory you want to generate the tree for.
- `-p`: (Optional) Only show directories, not files.
- `-a`: (Optional) Show both files and directories (this is the default behavior if no option is provided).

### Example:

```bash
python script.py /path/to/directory -p
```

This will print only the directories of the given path.

```bash
python script.py /path/to/directory
```

This will print both files and directories.

## Ignore List

The script uses an `ignore` file to exclude certain files and folders from the directory tree. The `ignore` file should be placed in the same directory as the script and contain the names of files or folders to be ignored, one per line.

Example `ignore` file:

```
__pycache__
build/
.git
*.txt
```

This will exclude:
- The `__pycache__` directory.
- Any directory named `build/`.
- The `.git` directory.
- Any file with a `.txt` extension.

If the `ignore` file is not provided, no files or folders will be ignored.

