from django.test import TestCase
from quickstart.models import Project
import unittest
import stringoperations.anagrams

# Create your tests here.

class Stringtestcases(unittest.TestCase):
    def test_anagram_list(self):
        words = ['this', 'is', 'a', 'real', 'tea', 'sentence', 'thing', 'ate', 'dusty', 'night', 'study', 'eat', 'tea']
        result = stringoperations.anagrams.get_anagrams(words)
        self.assertEqual(result, [['tea', 'ate', 'eat'], ['thing', 'night'], ['dusty', 'study']])

    def test_get_unique_list_will_not_add_element_if_element_is_present_in_list(self):
        dummy_list = ['test', 'check']
        result = stringoperations.anagrams.get_unique_list(dummy_list, 'test')
        self.assertEqual(result, ['test', 'check'])

    def test_get_unique_list_will_add_element_if_element_is_not_present_in_list(self):
        dummy_list = ['test', 'check']
        result = stringoperations.anagrams.get_unique_list(dummy_list, 'test1')
        self.assertEqual(result, ['test', 'check', 'test1'])

    def test_is_anagrams_return_true_if_the_list_consists_of_anagrams(self):
        words = ['thing', 'night']
        result = stringoperations.anagrams.is_anagrams(words)
        self.assertEqual(result, True)

    def test_is_anagrams_return_false_if_the_list_does_not_consists_of_anagrams(self):
        words = ['think', 'night']
        result = stringoperations.anagrams.is_anagrams(words)
        self.assertEqual(result, False)



