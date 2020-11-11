from naan_factory import NaanFactory # inherits from NaanFactory class

# class that will run the naan factory when called
class RunFactory(NaanFactory):

    def __init__(self):
        super().__init__() # inherits attributes and functions from parent class NaanFactory

    # function that runs make_dough() and then checks if bake_dough returns naan
    def run_factory(self):
        super().make_dough()
        if super().bake_dough() == "naan":
            return "Here's your naan" # if bake_dough() returns naan, a message is displayed informing the user
        else:
            return False # if naan isn't returned by bake_dough, it returns false, ending the loop