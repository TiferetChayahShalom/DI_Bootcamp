class Vehicle:
  def __init__(self, make, speed):
    self.make = make
    self.speed = speed # km/h

  def describe(self):
    print(f"{self.make} - top speed: {self.speed} km/h")

  def move(self):
    print(f"The {self.make} is moving.")

class Car(Vehicle):
  def __init__(self, make, speed, doors):
    super().__init__(make, speed)
    self.doors = doors

  def honk(self):
    print(f"The {self.make} goes: Beep beep!")

class ElectricCar(Car):
  def __init__(self, make, speed, doors, battery_kw):
    super().__init__(make, speed, doors)
    self.battery_kw = battery_kw

  def charge(self):
    print(f"Charging {self.make} - battery: {self.battery_kw} kW")


tesla = ElectricCar("Tesla Model 3", 250, 4, 75)
tesla.describe()
tesla.honk()
tesla.charge()

print(tesla.doors)

### 🌟 Exercise 1: Pets


class Pet:
  is_lazy = False

  def __init__(self, name, age):
    self.name = name
    self.age = age


  def description(self):
    print(f"{self.name} is {self.age} years old.")


  def make_sound(self):
    print("...")

class Cat(Pet):
  is_lazy = True

def __init__(self, name, age, indoor):
    super().__init__(name, age)
    self.indoor = indoor

def make_sound(self):
    print(f"{self.name} says: Meow!")


class Dog(Pet):
  is_lazy = False
    
def __init__(self, name, age, breed):

    super().__init__(name, age)
    self.breed = breed


def make_sound(self):
    print(f"{self.name} says: Woof!")


def fetch(self, item):
    print(f"{self.name} fetches the {item}!")


cat = Cat("Whiskers", 4, indoor=True)
dog = Dog("Buddy", 2, "Beagle")

cat.description()     # from Pet
cat.make_sound()      # Cat's version
dog.make_sound()      # Dog's version
dog.fetch("ball")

print(Cat.is_lazy)    # True
print(Dog.is_lazy)    # False (inherited from Pet)

