import unittest
from Virtual_Pet_Game import Dog, Cat, Bird, Fish, Bunny

class TestPetTypes(unittest.TestCase):
    def test_dog(self):
        dog = Dog("Buddy")
        self.assertEqual(dog.speak(), "Woof!")
    
    def test_cat(self):
        cat = Cat("Whiskers")
        self.assertEqual(cat.speak(), "Meow!")
    
    def test_bird(self):
        bird = Bird("Tweetie")
        self.assertEqual(bird.speak(), "Chirp!")
    
    def test_fish(self):
        fish = Fish("Bubbles")
        self.assertEqual(fish.speak(), "Blub!")
    
    def test_bunny(self):
        bunny = Bunny("Hoppy")
        self.assertEqual(bunny.speak(), "Hop!")


unittest.main()