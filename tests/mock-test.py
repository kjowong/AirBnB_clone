#!/usr/bin/python3
from mymodule import MyCLI
import unittest

from unittest.mock import create_autospec

class TestMyCLI(unittest.TestCase):
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return MyCLI(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def test_active(self):
        """Tesing `active` command"""
        cli = self.create()
        self.assertFalse(cli.onecmd("active"))
        self.assertTrue(self.mock_stdout.flush.called)
        self.assertEqual("Autogain active=False\n", self._last_write())
        self.mock_stdout.reset_mock()
        self.assertFalse(cli.onecmd("active TRue"))
        self.assertTrue(self.mock_stdout.flush.called)
        self.assertEqual("Autogain active=True\n", self._last_write())
        self.assertFalse(cli.onecmd("active 0"))
        self.assertTrue(self.mock_stdout.flush.called)
        self.assertEqual("Autogain active=False\n", self._last_write())

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("exit"))
        self.assertEqual("Goodbay\n", self._last_write())

if __name__ == '__main__':
    unittest.main()
