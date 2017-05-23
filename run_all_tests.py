import unittest
from os import path
import os

import glob
import unittest
from unittest import TestSuite


loader = unittest.TestLoader()
start_dir = "{}\\Testing\\".format(os.getcwd())
suite = loader.discover(start_dir, pattern='Test*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
