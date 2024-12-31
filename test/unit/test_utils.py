import unittest
from src.utils import fileExists, headerValidation

class TestUtils(unittest.TestCase):

  def test_fileExists(self):
    path = "./src"
    file = "utils.py"
    self.assertTrue(fileExists(path, file), "Error in fileExists implementation.\n Returned False when file exists.")

  def test_fileDoesNotExists(self):
    path = "./src"
    file = "foo.bar"
    self.assertFalse(fileExists(path, file), "Error in fileExists implementation.\n Returned True when file does not exist.")

  def test_folderDoesNotExist(self):
    path = "./foobar"
    file = "test.csv"
    self.assertFalse(fileExists(path, file), "Error in fileExists implementation.\n Returned True when folder does not exist.")

  def test_headerValidationEmptyCSV(self):
    headers = {"Red", "Blue"}
    self.assertRaises(NotImplementedError)
    #self.assertFalse(headerValidation("./test/data","emptySet.csv", headers), "Error in headerValidation. Returned True for empty CSV file.")

  def test_headerValidationEnptySet(self):
    headers = {}
    self.assertRaises(NotImplementedError)
    #self.assertFalse(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned True for empty header set.")

  def test_headerValidationMatch(self):
    headers = {"Red", "Blue"}
    self.assertRaises(NotImplementedError)
    #self.assertTrue(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned False when headers exist.")

  def test_headerValidationPartialMatch(self):
    headers = {"Red", "Pink"}
    self.assertRaises(NotImplementedError)
    #self.assertFalse(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned true when not all headers exist.")