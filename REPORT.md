# Virtual Pet Game
## Introduction
### What is Virtual Pet Game?
The **Virtual Pet Game** is a console-based simulation in which players adopt and care for digital pets with unique personalities and needs. Each pet has parameters like hunger and boredom, and players must manage these through interactions such as feeding, playing, and giving toys. The application is written in Python and demonstrates key Object-Oriented Programming (OOP) concepts and design patterns to create a modular and extensible codebase.
### How to run the game?
1. Ensure Python 3 is installed.
2. Save the game script as `virtual_pet_game.py`.
3. Open a terminal and run: `python virtual_pet_game.py`.
### How to play?
Upon launch, users interact with a text-based menu to:
1. Adopt a pet
2. Feed a pet
3. Play with a pet
4. Check on pets
5. Give a toy to a pet
6. Show pet's toys
7. Show my pets
8. Save game
9. Load game
0. (0) Quit
The player's objective is to maintain the pets’ well-being by managing their needs effectively.
## Analysis
### 4 OOP pillars, their meaning and usage (in code and overall)
1. Polymorphism: The most obvious example is the `speak()` method in the `VirtualPet(ABC)` class (each concrete pet class provides its own implementation of `speak()`. When `greet()` calls `speak()`, the appropriate version is called based on the actual object's type).
2. Abstraction: The `VirtualPet(ABC)` abstract base class (defines the common interface for all pets without providing complete implementation. Forces subclasses to implement 'speak()' making it abstract. Hides internal state (hunger, boredom) behind property decorators. Provides default implementations for shared behaviors such as `feed()`, `play()`, etc.).
