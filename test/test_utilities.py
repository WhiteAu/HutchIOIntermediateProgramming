import unittest

import hands_on.utilities as utilities
import pandas as pd

from unittest.mock import patch, Mock

class TestFileFunctions(unittest.TestCase):
    def setUp(self):
        print("add universal setup here!")

    def test_return_filetype_list(self):
        some_path = ""
        some_filetype = ""
        actual_value = utilities.return_filetype_list(some_path, some_filetype)

        print("add a test here!")

    def test_parse_list_for_doctors(self):
        test_input = []
        expected_output = []

        actual_output = utilities.parse_list_for_doctors(test_input)

    def test_check_for_doctors_in_csv(self):
        '''
        this should be a less 'mocked' test, ensuring that the integrated functions do what you think
        :return:
        '''

