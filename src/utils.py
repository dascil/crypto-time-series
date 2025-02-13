import os
import csv

def fileValidation(path: str, file:str) -> bool:
    """
    Checks if the file exists in the given directory.

    Args:
        path (str): Path to the folder containing the files.
        file (str): Name of the file.

    Returns:
        bool: True if file exist, False otherwise.
    """
    if not isinstance(path, str) or not isinstance(file, str) or not os.path.exists(path):
        return False

    return os.path.exists(os.path.join(path, file))

def headerValidation(path:str, file:str, headers:set) -> bool:
    """
    Checks to see if csv file in the data directory has the correct headers.
    Does not validate data.

    Args:
        path (str): Path to folder containing csv file
        file (str): Name of the csv dataset file
        headers (set): A set of the headers to check for existence of.

    Returns:
        bool: True if csv file contains the requested headers, False otherwise.
    """
    if not headers and not isinstance(headers, set):
        return False

    fullPath = os.path.join(path, file)
    csvHeaders = set()

    with open(fullPath, 'r') as dataset:
        reader = csv.reader(dataset)

        try:
            parseHeaders = next(reader)
            csvHeaders = set(header.strip() for header in parseHeaders)
        except StopIteration:
            return False

    return csvHeaders.issuperset(headers)

def csvValidation(path:str, file:str, headers:set) -> bool:
    """
    Checks to see if csv file is validated for use.
    Does not validate data.

    Args:
        path (str): Path to folder containing csv file
        file (str): Name of the csv dataset file
        headers (set): A set of the headers to check for existence of.

    Returns:
        bool: True if csv file contains the requested headers, False otherwise.
    """
    return fileValidation(path, file) and headerValidation(path, file, headers)