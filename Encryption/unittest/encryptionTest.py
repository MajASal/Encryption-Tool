import unittest
from Encryption.CesarEncryption import encoding
from Encryption.Monoalpha import monoEncryption


class TestCesarEncryption(unittest.TestCase):
    def test_encoding(self):

     result = encoding(1,"a")
     self.assertEqual("b", result, "b should be the result")


class TestMonoEncryption(unittest.TestCase):
     def test_Monoalpha(self):
      result = monoEncryption("Abc")
      self.assertEqual("zYX", result, "comment")


