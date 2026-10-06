class Cat:
# def_init_(self, cat_name, cat_ae):
 self.name = cat_name
 self.age = cat_age

 #cat1 = Cat("Fluffers", 3)
 #cat2 = Cat("Whiskey", 7)
 #cat3 = Cat("Mittens",1)

 # Step 2 :
 #def get_info(self):
 #return f"{self.name} is {self.age} years old."

 ---
### 🌟 Exercise 2: Dogs

#Now it's your turn to build the `Dog` class **from scratch**.

#**Step 1 — Create the Dog class:**
#- `__init__` takes `name` and `height` as parameters
#- `bark()` prints `"<name> goes woof!"`
- `jump()` prints `"<name> jumps <height*2> cm high!"`

#**Step 2 — Create two dog objects:**
#- `sarahs_dog` with name `"Bella"` and height `35`

#**Step 3 — Print details and call methods** for each dog

#**Step 4 — Compare their sizes** and print which is bigger

# 🌟 Exercise 2 — Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, height):
        self.name = dog_ name
        self.height = dog_height  # add attributes here

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create dog objects
# davids_dog = ...
# sarahs_dog = ...

# Step 3: Print details and call methods

# Step 4: Compare sizes



fluffy = Cat('Fluffy')
fluffy.make_sound() # fluffy carries its own name. Nothing to pass.

# Python sees: calle make_sound on fluffy -> self = fluffy

# my_list.sort()
# 'hello'.upper() # print "<name> goes woof!"

    def jump(self):
        pass  # print "<name> jumps <height*2> cm high!"

# Step 2: Create dog objects
# davids_dog = ...
# sarahs_dog = ...

# Step 3: Print details and call methods

# Step 4: Compare sizes

# 🌟 Exercise 3 — Song

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics  # store lyrics as attribute

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There's a place for us"])  # print each line

# Create a song and call sing_me_a_song()
# 🌟 Exercise 4 — Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

        

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        for animal in sorted(self.animals):
            letter - animal [0]
            if letter not in groups:
                groups[letter] = []
                goups[letter].append(animal)
    
    return groups
            

        pass  # return a dict grouped by first letter

    def get_groups(self):
        pass

# Create a zoo and test it
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()


