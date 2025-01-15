import unittest
from src.utils import fileValidation, headerValidation

class TestUtils(unittest.TestCase):

  def test_fileValidationFileExists(self):
    path = "./src"
    file = "utils.py"
    self.assertTrue(fileValidation(path, file), "Error in fileValidation implementation.\n Returned False when file exists.")

  def test_fileValidationFileDoesNotExists(self):
    path = "./src"
    file = "foo.bar"
    self.assertFalse(fileValidation(path, file), "Error in fileValidation implementation.\n Returned True when file does not exist.")

  def test_fileValidationFolderDoesNotExist(self):
    path = "./foobar"
    file = "test.csv"
    self.assertFalse(fileValidation(path, file), "Error in fileValidation implementation.\n Returned True when folder does not exist.")

  def test_fileValidationInvalidFolder(self):
    path = "foobar"
    file = "utils.py"
    self.assertFalse(fileValidation(path, file), "Error in fileValidation implementation.\n Returned True when invalid input for folder path.")

  def test_fileValidationInvalidFile(self):
    path = ".src"
    file = "util"
    self.assertFalse(fileValidation(path, file), "Error in fileValidation implementation.\n Returned True when invalid input for file name.")

  def test_fileValidationInvalidFile(self):
    path = None
    file = "util"
    self.assertFalse(fileValidation(path, file), "Error in fileValidation implementation.\n Returned True when None input for path.")

  def test_fileValidationInvalidFile(self):
    path = ".src"
    file = None
    self.assertFalse(fileValidation(path, file), "Error in fileValidation implementation.\n Returned True when None input for file name.")

  def test_headerValidationNonexistentFile(self):
    headers = {"Red", "Blue"}
    self.assertFalse(headerValidation("./test/data", "foobar.csv", headers), "Error in headerValidation. Returned True for file that does not exist.")

  def test_headerValidationEmptyCSV(self):
    headers = {"Red", "Blue"}
    self.assertFalse(headerValidation("./test/data","emptySet.csv", headers), "Error in headerValidation. Returned True for empty CSV file.")

  def test_headerValidationEmptySet(self):
    headers = {}
    self.assertFalse(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned True for empty header set.")

  def test_headerValidationMatch(self):
    headers = {"Red", "Blue"}
    self.assertTrue(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned False when headers exist.")

  def test_headerValidationPartialMatch(self):
    headers = {"Red", "Pink"}
    self.assertFalse(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned true when not all headers exist.")

  def test_headerValidationNoneHeaders(self):
    headers = None
    self.assertFalse(headerValidation("./test/data","headerSet.csv", headers), "Error in headerValidation. Returned true when not all headers exist.")

