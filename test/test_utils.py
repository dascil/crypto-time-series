import unittest
from utils import fileExists

class TestUtils(unittest.TestCase):
  def test_fileExists(self):
    path = "./src"
    file = "utils.py"

    self.assertTrue(fileExists(path, file), "Error in fileExists implementation.\nCannot detect file.")