#!/usr/bin/python3
""" Testing console """
from unittest.mock import create_autospec
from console import HBNBCommand
import unittest
import sys


class TestConsole(unittest.TestCase):
    """ testing test class """
    def setUp(self):
        """ mock stdin and stdout """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """ defining create method  """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """ defining exit test """
        cmd = self.create()
        self.assertRaises(SystemExit, quit)
