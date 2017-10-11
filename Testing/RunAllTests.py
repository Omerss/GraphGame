import unittest
from os import path
import os

import glob
import unittest
from unittest import TestSuite


loader = unittest.TestLoader()
suite = loader.discover(".", pattern='Test*.py')

runner = unittest.TextTestRunner()
runner.run(suite)
