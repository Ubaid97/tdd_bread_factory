
class NaanFactory:

    def __init__(self):
        self.ingredients = []
        self.ingredients.append(input("Please enter your first ingredient: ").lower())
        self.ingredients.append(input("Please enter your second ingredient: ").lower())

    def make_dough(self):
        if ("water" and "flour") in self.ingredients:
            return "dough"
        elif "water" in self.ingredients:
            print("you also need flour to make dough")
        elif "flour" in self.ingredients:
            print("you're also going to need some water to make dough")
        else:
            print("you need water and flour to make dough")

    def bake_dough(self):
        if self.make_dough() == "dough":
            return "naan"
        else:
            print("you need some dough")
            return False