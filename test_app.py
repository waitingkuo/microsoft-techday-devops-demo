from app import add
import unittest

class TestAddModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    
