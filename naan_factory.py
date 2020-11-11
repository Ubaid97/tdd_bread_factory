# class containing functions for making and baking dough
class NaanFactory:

    def __init__(self):
        self.ingredients = [] # an empty list to store ingredients input by the user
        # user asked to input two ingredients, both of which are added to the ingredients list
        self.ingredients.append(input("Please enter your first ingredient: ").lower())
        self.ingredients.append(input("Please enter your second ingredient: ").lower())

    # function that returns "dough" if water and flour are the ingredients input by the user
    def make_dough(self):
        # if statement which checks in the contents of the ingredients list
        if ("water" and "flour") in self.ingredients:
            return "dough" # if water and flour are in the list, returns dough
        elif "water" in self.ingredients:
            print("you also need flour to make dough") # if water is in the list but not flour, message is printed that flour is also needed
        elif "flour" in self.ingredients:
            print("you're also going to need some water to make dough") # if flour is in the list but not water, message is printed that water is also needed
        else:
            print("you need water and flour to make dough") # if neother water nor flour are in the list, user is told that they need both to make dough

    # function that returns "naan" if the make_dough() function returns "dough"
    def bake_dough(self):
        # if statement checks what value is returned by make_dough()
        if self.make_dough() == "dough":
            return "naan" # if make_dough() returns dough, naan is returned
        else:
            print("you need some dough") # if it doesn't return dough, user is told that they need dough
            return False