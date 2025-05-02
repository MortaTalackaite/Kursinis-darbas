import unittest
from unittest.mock import patch
from Virtual_Pet_Game import VirtualPet, Toy
from abc import ABC
import random

class TestVirtualPet(unittest.TestCase):
    def setUp(self):
        class ConcretePet(VirtualPet):
            def speak(self):
                return "Test"
        
        self.pet = ConcretePet("TestPet")
        self.toy = Toy("TestToy", 5)
    
    def test_abstract_base_class(self):
        self.assertTrue(issubclass(VirtualPet, ABC))
        with self.assertRaises(TypeError):
            VirtualPet("ShouldFail")
    
    def test_initial_state(self):
        self.assertEqual(self.pet.name, "TestPet")
        self.assertEqual(self.pet.hunger, 50)
        self.assertEqual(self.pet.boredom, 50)
        self.assertEqual(len(self.pet.show_toys()), 0)
    
    def test_feed(self):
        self.pet.feed()
        self.assertEqual(self.pet.hunger, 75)
    
    def test_play(self):
        self.pet.play()
        self.assertEqual(self.pet.boredom, 75)
    
    def test_add_toy(self):
        self.pet.add_toy(self.toy)
        self.assertEqual(self.pet.boredom, 55)
    
    @patch('builtins.print')
    def test_changes(self, mock_print):
        with patch.object(random, 'randint', side_effect=[2, 2]):
            self.pet.changes()
            self.assertEqual(self.pet.hunger, 48)
            self.assertEqual(self.pet.boredom, 48)


unittest.main()