import unittest
from Virtual_Pet_Game import Toy

class TestToy(unittest.TestCase):
    def setUp(self):
        self.toy = Toy("Ball", 10)
    
    def test_toy_initialization(self):
        self.assertEqual(self.toy.name, "Ball")
        self.assertEqual(self.toy.fun_value, 10)
    
    def test_toy_properties(self):
        self.assertEqual(self.toy.name, "Ball")
        self.assertEqual(self.toy.fun_value, 10)
    
    def test_toy_immutability(self):
        with self.assertRaises(AttributeError):
            self.toy.name = "NewName"
        with self.assertRaises(AttributeError):
            self.toy.fun_value = 20


unittest.main()