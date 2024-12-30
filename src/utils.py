import os

def fileExists(directory: str, file:str) -> bool:
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

def headerValidation(file:str, headers:set) -> bool:
    """
    Checks to see if csv file in the data directory has the correct headers.

    Args:
        file (str): Name of the csv dataset file
        headers (set): A set of the headers to check for existence of.

    Returns:
        bool: True if csv file contains the requested headers, False otherwise.
    """

    return NotImplementedError

