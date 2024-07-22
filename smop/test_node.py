import unittest
from smop.node import decode

class TestNodeFunctions(unittest.TestCase):

    def test_decode_single_underscore(self):
        class MockNode:
            name = "_"
        self.assertEqual(decode(MockNode()), "")

    def test_decode_underscore_followed_by_single_char(self):
        class MockNode:
            name = "_a"
        self.assertEqual(decode(MockNode()), "A")

    def test_decode_underscore_followed_by_multiple_chars(self):
        class MockNode:
            name = "_abc"
        self.assertEqual(decode(MockNode()), "Abc")

if __name__ == '__main__':
    unittest.main()
