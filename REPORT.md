# Virtual Pet Game

## Introduction

### What is Virtual Pet Game?

The **Virtual Pet Game** is a console-based simulation in which players adopt and care for digital pets with unique personalities and needs. Each pet has its own needs  (hunger and boredom). Players must manage pet's needs through interactions such as feeding, playing, and giving toys. The application is written in Python and demonstrates key Object-Oriented Programming (OOP) concepts and design patterns to create a modular and extensible code.

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
0. Quit

#### The player's objective is to maintain the pets’ well-being by managing their needs effectively.

## Analysis

### 4 OOP pillars, their meaning and usage

#### Polymorphism

The most obvious example is the `speak()` method in the `VirtualPet(ABC)` class (each concrete pet class provides its own implementation of `speak()`. When `greet()` calls `speak()`, the appropriate version is called based on the actual object's type).

#### Abstraction

The `VirtualPet(ABC)` abstract base class (defines the common interface for all pets without providing complete implementation. Forces subclasses to implement `speak()` making it abstract. Hides internal state (hunger, boredom) behind property decorators. Provides default implementations for shared behaviors such as `feed()`, `play()`, etc.).

#### Inheritance

The `VirtualPet(ABC)` class is an **abstract base class (parent class)** that defines the common structure and behavior for all pets (defines common attributes (`name`, `hunger`, `boredom`, `toys`). Provides default implementations (`feed()`, `play()`). Forces subclasses to implement `speak()` (using `@abstractmethod`)).

#### Encapsulation

Private attributes (attributes are marked as **private** using double underscores (`__`), preventing direct external access. Access is controlled through **getter methods** using `@property` decorators).

### Design patterns

1. **Factory Method**: `PetFactory` class (hides the complex pet creation logic).
2. **Decorator**: `PetDecorator` class (adds new behaviors without modifying original classes.).

### Composition

1. **Pets own their toys** (if a pet is deleted, its toys disappear).
2. **PetDecorator owns its enhanced pet** (decorator controls the enhanced pet's lifecycle).

### Aggregation

1. **Owner aggregates pets** (pets can exist without an owner).
2. **Game aggregates pets and toys** (they can be reused/reassigned)

### Reading from file & writing to file

Game implements file operations to save/load game states using simple text files.

#### `save_game(player, pets, filename = "virtual_pet_game.txt")` method

Saves player's name and pet details (uses `with open()` for **auto-closing the file** after writing. Writes data in a structured format. Handles errors).

#### `load_game(filename="virtual_pet_game.txt")` method

Loads saved data (validates file's existence before reading. Parses each line to reconstruct pets. Handles errors). 

## Results

### Game Works as Intended

1. Players can adopt pets, manage their needs by feeding, playing or giving toys to their pets.
2. Pet's hunger and boredom levels change over time.
3. Pets are created randomly.
4. Some pets get enhanced attributes.
5. Game progress can be saved to/loaded from a text file.

### Neccesssary OOP principles

1. **Encapsulation** keeps attributes private.
2. **Inheritance** core code logic is shared to subclasses.
3. **Polymorphism** allows method overriding.
4. **Abstraction** hides complexity.

### Factory Method and Decorator design patterns

Help to maintain a "clean" code.

## Summary

