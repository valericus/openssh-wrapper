import unittest

import openssh_wrapper


class TestSeparateFunctions(unittest.TestCase):
    def test_b(self):
        input_value = 'abcd'
        expected_result = b'abcd'
        self.assertEqual(expected_result, openssh_wrapper.b(input_value))
        input_value = u'abcd'
        expected_result = b'abcd'
        self.assertEqual(expected_result, openssh_wrapper.b(input_value))
        input_value = b'abcd'
        expected_result = b'abcd'
        self.assertEqual(expected_result, openssh_wrapper.b(input_value))

    def test_u(self):
        input_value = b'abcd'
        expected_result = 'abcd'
        self.assertEqual(expected_result, openssh_wrapper.u(input_value))
        input_value = u'abcd'
        expected_result = 'abcd'
        self.assertEqual(expected_result, openssh_wrapper.u(input_value))
        input_value = 'abcd'
        expected_result = 'abcd'
        self.assertEqual(expected_result, openssh_wrapper.u(input_value))

    def test_b_list(self):
        input_value = ['abcd', u'efgh', b'ijkl']
        expected_result = [b'abcd', b'efgh', b'ijkl']
        self.assertEqual(expected_result, openssh_wrapper.b_list(input_value))

    def test_u_list(self):
        input_value = ['abcd', u'efgh', b'ijkl']
        expected_result = ['abcd', 'efgh', 'ijkl']
        self.assertEqual(expected_result, openssh_wrapper.u_list(input_value))

    def test_b_quote(self):
        # TODO Seems this test does something wrong, 'cause I'm not sure
        # what this function is for
        input_value = ['abcd', u'efgh', b'ijkl']
        expected_result = ['abcd', 'efgh', 'ijkl']
        self.assertEqual(expected_result, openssh_wrapper.u_list(input_value))
