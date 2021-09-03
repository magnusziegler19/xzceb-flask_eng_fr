import unittest

from translator import *

class test_e2f(unittest.TestCase):
    def test_null(self):
        self.assertEqual(english_to_french(''), '')
        
    def test_word(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class test_f2e(unittest.TestCase):
    def test_null(self):
        self.assertEqual(french_to_english(''), '')
        
    def test_word(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()