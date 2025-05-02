import random
from abc import ABC, abstractmethod
from pathlib import Path

class Toy:
    def __init__(self, name, fun_value):
        self.__name = name
        self.__fun_value = fun_value

    @property
    def name(self):
        return self.__name
    
    @property
    def fun_value(self):
        return self.__fun_value


class Owner:
    def __init__(self, name):
        self.__name = name
        self.__pets = []

    @property
    def name(self):
        return self.__name

    @property
    def pets(self):
        return self.__pets


class VirtualPet(ABC):
    def __init__(self, name):
        self.__name = name
        self.__hunger = 50
        self.__boredom = 50
        self.__toys = []

    def add_toy(self, toy):
        self.__toys.append(toy)
        self.__boredom = min(100, self.__boredom + toy.fun_value)
        print(f"\n{self.__name} got a {toy.name}!")

    def show_toys(self):
        if not self.__toys:
            print(f"\n{self.__name} doesn't have any toys.")

        else:
            print(f"\n{self.__name}'s toys:")

            for toy in self.__toys:
                print(f"{toy.name}")
        return self.__toys

    @property
    def name(self):
        return self.__name

    @property
    def hunger(self):
        return self.__hunger

    @property
    def boredom(self):
        return self.__boredom

    @abstractmethod
    def speak(self):
        pass

    def greet(self):
        print(f"{self.__name} the {self.__class__.__name__} says: {self.speak()}")

    def changes(self):
        was_hungry = self.__hunger < 50
        was_bored = self.__boredom < 50
    
        self.__hunger -= random.randint(1,3)
        self.__boredom -= random.randint(1,3)

        if not was_hungry and self.__hunger < 50 and self.__hunger > 0:
            print(f"{self.__name} is hungry.")

        elif self.__hunger < 1:
            print(f"{self.__name} went to Heaven.")

        if not was_bored and self.__boredom < 50 and self.__boredom >= 10:
            print(f"{self.__name} is bored.")

        elif self.__boredom < 10:
            print(f"{self.__name} ran away and found a fun owner.")

    def feed(self):
        self.__hunger = min(100, self.__hunger + 25)
        print(f"You fed {self.__name}.")

    def play(self):
        self.__boredom = min(100, self.__boredom + 25)
        print(f"You played with {self.__name}.")


class PetDecorator(VirtualPet):
    def __init__(self, pet):
        self._pet = pet
        
    @property
    def name(self):
        return self._pet.name
    
    @property
    def pet_type(self):
        return self._pet.__class__.__name__
        
    @property
    def hunger(self):
        return self._pet.hunger
        
    @property
    def boredom(self):
        return self._pet.boredom
        
    def speak(self):
        return self._pet.speak()
        
    def greet(self):
        print(f"{self.name} the {self.pet_type} says: {self.speak()}")
        
    def changes(self):
        self._pet._VirtualPet__hunger -= random.randint(1, 2)
        self._pet._VirtualPet__boredom -= random.randint(1, 2)
        return self._pet.changes()
        
    def feed(self):
        self._pet._VirtualPet__hunger = min(100, self._pet.hunger + 30)
        print(f"You fed {self.name}. They really enjoyed it!")
        
    def play(self):
        self._pet._VirtualPet__boredom = min(100, self._pet.boredom + 30)
        print(f"You played with {self.name}. They had extra fun!")
        
    def add_toy(self, toy):
        return self._pet.add_toy(toy)
        
    def show_toys(self):
        return self._pet.show_toys()


class Dog(VirtualPet):
    def speak(self):
        return "Woof!"


class Cat(VirtualPet):
    def speak(self):
        return "Meow!"


class Bird(VirtualPet):
    def speak(self):
        return "Chirp!"


class Fish(VirtualPet):
    def speak(self):
        return "Blub!"


class Bunny(VirtualPet):
    def speak(self):
        return "Hop!"


class PetFactory:
    @staticmethod
    def create_pet(name):
        pet_classes = [Dog, Cat, Bird, Fish, Bunny]
        pet_type = random.choice(pet_classes)
        base_pet = pet_type(name)
        
        if random.random() < 0.3:
            return PetDecorator(base_pet)
            
        return base_pet


def save_game(player, pets, filename = "virtual_pet_game.txt"):
    try:
        with open(filename, 'w') as file:
            file.write(f"PLAYER: {player.name}\n")

            saved_pets = set()
            for pet in pets:
                base_pet = pet._pet if isinstance(pet, PetDecorator) else pet
                if base_pet.name not in saved_pets:
                    file.write(f"PET: {base_pet.name} the {base_pet.__class__.__name__}, hunger: {base_pet.hunger}, boredom: {base_pet.boredom}\n")
                    saved_pets.add(base_pet.name)

        print(f"Game saved successfully to {filename}!")
        return True
        
    except Exception as e:
        print(f"Error saving game: {e}")
        return False


def load_game(filename = "virtual_pet_game.txt"):
    try:
        import os
        if not os.path.exists(filename):
            print("No saved game found")
            return None, []
        
        with open(filename, 'r') as file:
            player = None
            pets = []
            
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                if line.startswith("PLAYER:"):
                    player_name = line[7:].strip()
                    player = Owner(player_name)
                
                elif line.startswith("PET:"):
                    pet_data = line[4:].strip()
                    name_part, rest = pet_data.split(" the ", 1)
                    pet_name = name_part.strip()
                    
                    pet_type_part, stats_part = rest.split(",", 1)
                    pet_type = pet_type_part.strip()
                    
                    hunger_part, boredom_part = stats_part.split(",")
                    hunger = int(hunger_part.replace("hunger:", "").strip())
                    boredom = int(boredom_part.replace("boredom:", "").strip())
                    
                    pet_classes = {
                        "Dog": Dog, "Cat": Cat, "Bird": Bird,
                        "Fish": Fish, "Bunny": Bunny
                    }
                    
                    if pet_type in pet_classes:
                        pet = pet_classes[pet_type](pet_name)
                        pet._VirtualPet__hunger = hunger
                        pet._VirtualPet__boredom = boredom
                        
                        if random.random() < 0.3:
                            pet = PetDecorator(pet)
                            
                        pets.append(pet)
            
            if player and pets:
                player._Owner__pets = pets
                print("Game loaded successfully!")
                return player, pets
                
            else:
                print("Save file is incomplete")
                return None, []
                
    except Exception as e:
        print(f"Error loading game: {str(e)}")
        return None, []


def main():
    pets = []
    player = Owner("Player 1")
    available_toys = [Toy("Ball", 10), Toy("Chew Toy", 15), Toy("Feather", 8)]
    print("\nWelcome to the Pet Store!")

    while True:
        print("\nMenu:")
        print("1. Adopt a pet")
        print("2. Feed a pet")
        print("3. Play with a pet")
        print("4. Check on pets")
        print("5. Give a toy to a pet")
        print("6. Show pet's toys")
        print("7. Show my pets")
        print("8. Save game")
        print("9. Load game")
        print("0. Quit")

        choice = input("\nWhat would you like to do? ")

        if choice == "1":
            name = input("\nWhat would you like to name your pet? ")
            pet = PetFactory.create_pet(name)
            player.pets.append(pet)

            if pet not in pets:
                pets.append(pet)
                print(f"\nYou adopted a {pet.__class__.__name__}!")
                pet.greet()

        elif choice == "2":
            if not player.pets:
                print("\nNo pets to feed!")

            else:
                print("\nYour pets:")

                for pet in player.pets:
                    print(f"{pet.name} (Hunger: {pet.hunger})")

                name = input("\nEnter the name of the pet to feed: ")
                found = False

                for pet in player.pets:
                    if pet.name.lower() == name.lower():
                        pet.feed()
                        found = True
                        break

                if not found:
                    print(f"\nNo pet named {name} found!")
        
        elif choice == "3":
            if not player.pets:
                print("\nNo pets to play with!")

            else:
                print("\nYour pets:")

                for pet in player.pets:
                    print(f"{pet.name} (Boredom: {pet.boredom})")

                name = input("\nEnter the name of the pet to play with: ")
                found = False

                for pet in player.pets:
                    if pet.name.lower() == name.lower():
                        pet.play()
                        found = True
                        break

                if not found:
                    print(f"\nNo pet named {name} found!")

        elif choice == "4":
            if not player.pets:
                print("\nNo pets yet!")

            else:
                for pet in player.pets:
                    print(f"\n{pet.name} | Hunger: {pet.hunger}, Boredom: {pet.boredom}")

        elif choice == "5":
            if not player.pets:
               print("\nNo pets available.")
               continue

            print("\nAvailable toys:")

            for toy in available_toys:
                print(f"{toy.name}")
                
            pet_name = input("\nEnter the name of the pet to give a toy to: ")
            toy_name = input("Enter the name of the toy to give to the pet: ")

            selected_toy = None

            for toy in available_toys:
                if toy.name.lower() == toy_name.lower():
                    selected_toy = toy
                    break

            if selected_toy is None:
                print("\nInvalid toy name.")
                continue

            selected_pet = None

            for pet in player.pets:
                if pet.name.lower() == pet_name.lower():
                    selected_pet = pet
                    break

            if selected_pet is None:
                print("\nInvalid pet name.")
                continue
            
            selected_pet.add_toy(selected_toy)
            
            if selected_pet not in pets:
                pets.append(selected_pet)
        
        elif choice == "6":
            pet_name = input("\nEnter the name of the pet to show toys for: ")
            found = False

            for pet in pets:
                if pet.name.lower() == pet_name.lower():
                    pet.show_toys()
                    found = True
                    break

            if not found:
                print(f"\nNo pet named {pet_name} found!")

        elif choice == "7":
            print(f"\n{player.name}'s pets:")

            for pet in player.pets:
                if isinstance(pet, PetDecorator):
                    print(f"{pet.name} the {pet.pet_type} (Enhanced)")
                else:
                    print(f"{pet.name} the {pet.__class__.__name__}")

        elif choice == "8":
            save_game(player, pets)
            
        elif choice == "9":
                loaded_player, loaded_pets = load_game()
                if loaded_player:
                    player = loaded_player
                    pets = loaded_pets
                
        elif choice == "0":
            save_choice = input("Save before quitting? (y/n): ").lower()

            if save_choice == 'y':
                save_game(player, pets)
                print("\nGoodbye!")
                break

            elif save_choice == 'n':
                print("\nGoodbye!")
                break

        else:
            print("\nInvalid choice")

        for pet in pets:
            pet.changes()


main()
