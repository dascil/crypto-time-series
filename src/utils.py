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

