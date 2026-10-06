---
### 🌟 Exercise 2: Dogs

#Create two classes: `Dog` and `Dogs` (a collection).

Class Dog:
 def __init_(self,name, age, weight, breed):
  self.name = name
  self.age = age
  self.weight = weight
  self.breed = breed

def run_speed(self):
    return (self.weight / self.age) * 10

def fight(self, other_dog):
    my_speed = self.run_speed()
    their_speed = other_dog.run_speed()
    if my_speed > their_speed:
        print(f"{self.name} wins!")
    elif their_speed > my_speed:
        print(f"{other_dog.name} wins!")
    else:
        print("It's a draw!")




    #if speed1 > speed2:
       # print(f"{self.name} wins!")
    #elif speed2 > speed1:
    #    print(f"{other_dog.name} wins!")
    #else:
        #print("It's a draw!")

Class Dogs:
def__init__(self):
        self.pack = []

def add_dog(self, dog):
        self.pack.append(dog)

def fight_all(self):
        for i in range(len(self.pack)):
            for j in range(i + 1, len(self.pack)):
                self.pack[i].fight(self.pack[j])

#**Test:**

d1 = Dog("Rex",   4, 20.0, "German Shepherd")
d2 = Dog("Bella", 2, 12.0, "Poodle")
d3 = Dog("Max",   6, 30.0, "Saint Bernard")

pack = Dogs()
pack.add_dog(d1)
pack.add_dog(d2)
pack.add_dog(d3)
pack.fight_all()
break

---
### 🌟 Exercise 3: PetDog — Inheritance + `super()` + `*args` + `random`

#Build on your `Dog` class from Exercise 2 by creating a child class `PetDog`.
import random
Class PetDog(Dog):
 def __init_(self, name, age, weight, breed, *tricks):
    k

akes: `name`, `age`, `weight`, `breed`, `*tricks`
  - Call `super().__init__()` with the first four arguments
  - Store `self.tricks = list(tricks)` ← the extra `*args`
- Method `learn_trick(trick)` → appends `trick` to `self.tricks`
- Method `show_tricks()`:
  - If no tricks: prints `"<name> doesn't know any tricks yet."`
  - Otherwise: prints each trick on a separate line, numbered from 1
- Method `do_random_trick()`:
  - **Import `random`** at the top of the cell
  - If no tricks: prints `"<name> shrugs."`
  - Otherwise: uses `random.choice(self.tricks)` and prints `"<name> performs: <trick>!"`

**Test:**
```python
import random

sparky = PetDog("Sparky", 3, 8.0, "Jack Russell", "sit", "paw")
sparky.show_tricks()
sparky.learn_trick("roll over")
sparky.show_tricks()
sparky.do_random_trick()

# Also confirm inherited methods still work:
print(sparky.run_speed())
break

class Player:
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists

 break
---
### 🌟 Exercise 4: Family & Person

#Model a family using **composition** — a `Family` that contains `Person` objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I'm {self.age} years old.")

class Family:
    def __init__(self, surname):
        self.surname = surname
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def greet_all(self):
        for member in self.members:
            member.greet()

    def find_oldest(self):
        oldest = self.members[0]
        for member in self.members:
            if member.age > oldest.age:
                oldest = member
        return oldest

    def average_age(self):
        if not self.members:
            return 0.0
        total_age = sum(member.age for member in self.members)
        return total_age / len(self.members)
  - If no members, return `0.0`

#**Test:**

family = Family("Smith")
family.add_member(Person("Alice", 45))
family.add_member(Person("Bob",   47))
family.add_member(Person("Carol", 17))
family.add_member(Person("Dan",   14))

family.greet_all()
oldest = family.find_oldest()
print(f"Oldest: {oldest.name}")
print(f"Average age: {family.average_age():.1f}")



# 🌟 Exercise 4: Family & Person
# Your code here


#METHOD CHAINING — return self enables it
══════════════════════════════════════════════════════════════════════

  WITHOUT return self:                WITH return self:

  obj.set_name("Alice")               obj.set_name("Alice")
  obj.set_age(30)                         .set_age(30)
  obj.set_email("a@b.com")               .set_email("a@b.com")
  # must repeat 'obj' every time      # clean chain — same object throughout


  class Builder:
      def __init__(self):
          self.name  = None
          self.age   = None
          self.email = None

      def set_name(self, name):
          self.name = name
          return self       ← key: return the object itself

      def set_age(self, age):
          self.age = age
          return self       ← same here

      def set_email(self, email):
          self.email = email
          return self       ← same here

  b = Builder()
  b.set_name("Alice").set_age(30).set_email("a@b.com")   ← each call returns b

  
