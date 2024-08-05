import unittest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
from smop.main import main
from smop import options

class TestMainFunction(unittest.TestCase):
    def setUp(self):
        options.filelist = []
        options.output = None
        options.no_header = False
        options.xfiles = []
        options.strict = False
        options.verbose = False
        options.no_resolve = False
        options.no_backend = False
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_main_handles_file_lists_correctly(self):
        options.filelist = ['test.m', 'ignore.txt', 'excluded.m']
        options.xfiles = ['excluded.m']
        with patch('builtins.open', mock_open(read_data='data')):
            main()
        self.assertIn("Ignored: 'ignore.txt'", self.held_stdout.getvalue())

    def test_main_writes_to_stdout_when_output_option_is_set_to_minus(self):
        options.output = '-'
        main()
        self.assertNotEqual("", self.held_stdout.getvalue())

    def test_main_correctly_handles_errors_and_continues(self):
        options.filelist = ['test.m', 'error.m']
        options.strict = False
        with patch('builtins.open', mock_open(read_data='data')), patch('smop.parse.parse', side_effect=[None, Exception('Test Error')]):
            main()
        self.assertIn("Errors: 1", self.held_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
