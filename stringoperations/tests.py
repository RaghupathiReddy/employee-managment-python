from django.test import TestCase
from quickstart.models import Project
import unittest
import stringoperations.anagrams

# Create your tests here.

class Stringtestcases(unittest.TestCase):
    def test_anagram_success_case(self):
        result = stringoperations.anagrams.anagramList('test and Dan thing night')
        self.assertEqual(result, [['and', 'Dan'], ['thing', 'night']])
