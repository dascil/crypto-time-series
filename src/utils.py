import os

def fileValidation(directory: str, file:str) -> bool:
    """
    Checks if the file exists in the given directory.

    Args:
        directory (str): Path to the folder containing the files.
        file (str): Name of the file.

    Returns:
        bool: True if file exist, False otherwise.
    """
    if not os.path.exists(directory):
        return False

    return os.path.exists(os.path.join(directory, file))

def headerValidation(path:str, file:str, headers:set) -> bool:
    """
    Checks to see if csv file in the data directory has the correct headers.

    Args:
        path (str): Path to folder containing csv file
        file (str): Name of the csv dataset file
        headers (set): A set of the headers to check for existence of.

    Returns:
        bool: True if csv file contains the requested headers, False otherwise.
    """
    # isValidFile = fileExists(path, file)
    # if not isValidFile:
    #     return False
    return NotImplementedError

