import unittest
from unittest.mock import patch
from Virtual_Pet_Game import PetFactory, PetDecorator, Dog

class TestPetFactory(unittest.TestCase):
    @patch('random.choice')
    @patch('random.random')
    def test_create_pet(self, mock_random, mock_choice):
        mock_random.return_value = 0.5
        mock_choice.return_value = Dog
        pet = PetFactory.create_pet("Buddy")
        self.assertIsInstance(pet, Dog)
        
        mock_random.return_value = 0.2
        pet = PetFactory.create_pet("Lucky")
        self.assertIsInstance(pet, PetDecorator)
        self.assertIsInstance(pet._pet, Dog)


unittest.main()