import unittest
from unittest.mock import patch
from Virtual_Pet_Game import PetDecorator, Cat
import random

class TestPetDecorator(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Fluffy")
        self.decorated_cat = PetDecorator(self.cat)
    
    def test_delegation(self):
        self.assertEqual(self.decorated_cat.name, "Fluffy")
        self.assertEqual(self.decorated_cat.speak(), "Meow!")
    
    def test_enhanced_feed(self):
        initial_hunger = self.decorated_cat.hunger
        self.decorated_cat.feed()
        self.assertEqual(self.decorated_cat.hunger, initial_hunger + 30)
    
    def test_enhanced_play(self):
        initial_boredom = self.decorated_cat.boredom
        self.decorated_cat.play()
        self.assertEqual(self.decorated_cat.boredom, initial_boredom + 30)
    
    @patch('builtins.print')
    def test_enhanced_changes(self, mock_print):
        with patch.object(random, 'randint', return_value=1):
            self.decorated_cat.changes()
            self.assertEqual(self.decorated_cat.hunger, 48)
            self.assertEqual(self.decorated_cat.boredom, 48)


unittest.main()