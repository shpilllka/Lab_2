from abc import ABC, abstractmethod

class Pet(ABC):      # абстрактный класс
    @abstractmethod
    def make_noise(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass


class Animal(Pet, ABC):       # абстрактный класс, наследуется от Pet и ABC
    def __init__(self, name):
        self._name = name       # "_" перед названием = protected поле, доступ к ним через get-метод
    
    def get_name(self):
        return self._name


class Turtle(Animal):       # наследуется от Animal
    def __init__(self, name):
        super().__init__(name)
    
    def make_noise(self):
        print("""  _____     ____
 /      \\  |  o | 
|        |/ ___\\| 
|_________/     
|_|_| |_|_|""")
        

class Parrot(Animal):         # наследуется от Animal
    def __init__(self, name):
        super().__init__(name)
    
    def make_noise(self):
        print("""       /////
     ( - v - )
  (  )      (  ) 
      v.   v""")
        

class Person:
    def __init__(self, pet: Pet, name: str):
        self._pet = pet
        self._name = name
    
    def set_pet(self, pet: Pet):
        self._pet = pet
    
    def get_pet_info(self):
        print("--------------------")
        print(f"Pet for {self._name} is named {self._pet.get_name()}")
        print("And it sounds like this:")
        self._pet.make_noise()           # ПОЛИМОРФИЗМ
        print("--------------------")

# Полиморфизм: класс Person работает с абстракцией Pet;
#              метод get_pet_info (стр52) вызывает make_noise() (стр56),
#              не зная, какое именно животное там находится


def main():
    parrot = Parrot("Kesha")
    turtle = Turtle("Zavala")
    
    jack = Person(parrot, "Jack")
    john = Person(turtle, "John")
    
    jack.get_pet_info()
    john.get_pet_info()

if __name__ == "__main__":
    main()
