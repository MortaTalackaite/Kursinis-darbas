import unittest
import os
from io import StringIO
from unittest.mock import patch
from Virtual_Pet_Game import Owner, Cat, save_game, load_game

class TestSaveLoad(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_save.txt"
        self.player = Owner("Test Player")
        self.pet = Cat("Fluffy")
        self.player.pets.append(self.pet)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_save_game(self):
        result = save_game(self.player, [self.pet], self.test_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_file))
        
        with open(self.test_file, 'r') as f:
            content = f.read()
            self.assertIn("PLAYER: Test Player", content)
            self.assertIn("PET: Fluffy the Cat", content)
    
    def test_load_game(self):
        with open(self.test_file, 'w') as f:
            f.write("PLAYER: Loaded Player\n")
            f.write("PET: LoadedPet the Dog, hunger: 60, boredom: 40\n")
        
        player, pets = load_game(self.test_file)
        self.assertEqual(player.name, "Loaded Player")
        self.assertEqual(len(pets), 1)
        self.assertEqual(pets[0].name, "LoadedPet")
        self.assertEqual(pets[0].hunger, 60)
        self.assertEqual(pets[0].boredom, 40)
    
    def test_load_nonexistent_file(self):
        player, pets = load_game("nonexistent.txt")
        self.assertIsNone(player)
        self.assertEqual(len(pets), 0)


unittest.main()