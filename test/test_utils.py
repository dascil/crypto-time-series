import unittest
from src.utils import fileExists

class TestUtils(unittest.TestCase):

  def test_fileExists(self):
    path = "./src"
    file = "utils.py"

    self.assertTrue(fileExists(path, file), "Error in fileExists implementation.\nCannot detect file.")

  def test_trainingSetExists(self):
    path = "./data"
    file = "training.csv"

    self.assertTrue(fileExists(path, file), "Training set does not exist or is not in a csv format.")

  def test_testSetExists(self):
    path = "./data"
    file = "test.csv"

    self.assertTrue(fileExists(path, file), "Test set does not exist or is not in a csv format.")

    # TODO: Add test cases for CSV Validation