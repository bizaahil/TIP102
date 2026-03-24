class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if (len(new_catchphrase) < 20 and all(x.isalpha() or x.isspace() for x in new_catchphrase)):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("invalid catchphrase")

    def add_item(self, item_name):
        my_set = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}
        if item_name in my_set:
            self.furniture.append(item_name)

    def print_inventory(self):
        my_dict = {}

        for furniture in self.furniture:
            if furniture not in my_dict:
                my_dict[furniture] = 1
            else:
                my_dict[furniture] += 1

        if len(my_dict) == 0:
            print("Inventory empty")
        for item in my_dict:
            print(item, my_dict[item])


alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "Pah")
bones = Villager("Bones", "Dog", "yip yap")

print(apollo.greet_player("Ash"))
print(bones.greet_player("Steve"))

bones.catchphrase = "ruff it up"
print(bones.greet_player("Steve"))

print(apollo.name)
print(apollo.species)
print(apollo.catchphrase)
print(apollo.furniture)

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()

# Question 2