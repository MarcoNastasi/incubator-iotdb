#!/usr/bin/env python3
import unittest
import subprocess
import os

class TestBasic(unittest.TestCase):

    def test_functionality(self):
        path = os.path.dirname(os.path.realpath(__file__))
        self.assertEqual(subprocess.run(['python3', f'{path}/../src/client_example.py']).returncode, 0)


if __name__ == '__main__':
    unittest.main()