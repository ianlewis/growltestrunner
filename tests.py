#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest

from testrunner import NotifyTestRunner

class DemoTest(unittest.TestCase):
    """
    """
    def test_true(self):
        """
        """
        self.assert_(True)
    def test_false(self):
        """
        """
        self.assert_(False)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DemoTest)
    NotifyTestRunner().run(suite)
