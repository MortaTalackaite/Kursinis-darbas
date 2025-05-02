import unittest
from Virtual_Pet_Game import Owner, Cat

class TestOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("Test Owner")
        self.pet = Cat("Fluffy")
    
    def test_owner_initialization(self):
        self.assertEqual(self.owner.name, "Test Owner")
        self.assertEqual(len(self.owner.pets), 0)
    
    def test_add_pet(self):
        self.owner.pets.append(self.pet)
        self.assertEqual(len(self.owner.pets), 1)
        self.assertEqual(self.owner.pets[0].name, "Fluffy")
    
    def test_owner_properties(self):
        self.assertEqual(self.owner.name, "Test Owner")
        with self.assertRaises(AttributeError):
            self.owner.name = "New Name"


unittest.main()