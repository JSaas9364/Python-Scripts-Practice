class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"{self.name} (Weight: {self.weight}, Value: {self.value})"


class Bag:
    def __init__(self, character_level):
        self.character_level = character_level
        self.max_weight = 10 + (character_level * 5)  # Base 10 + 5 per level
        self.items = []
        self.current_weight = 0

    def add_item(self, item):
        if self.current_weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.current_weight += item.weight
            print(f"Added {item.name} to bag.")
        else:
            print(f"Cannot add {item.name}. Not enough space!")

    def show_inventory(self):
        print("\n=== Inventory ===")
        if not self.items:
            print("Bag is empty.")
        else:
            for item in self.items:
                print(f"- {item.name} (Weight: {item.weight}, Value: {item.value})")
        print(f"Total Weight: {self.current_weight}/{self.max_weight}\n")


# === Example Usage ===
character_level = int(input("Enter character level: "))  # User inputs character level
bag = Bag(character_level)  # Create bag with level-based weight limit

# Creating medieval game items
items = [
    Item("Iron Sword", 10, 150),
    Item("Steel Shield", 15, 200),
    Item("Healing Potion", 2, 50),
    Item("Magic Scroll", 1, 300),
    Item("Golden Chalice", 5, 500),
    Item("Leather Armor", 8, 120),
]

# Adding items to the bag
for item in items:
    bag.add_item(item)

# Displaying inventory
bag.show_inventory()
