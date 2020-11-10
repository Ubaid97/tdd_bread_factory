from naan_factory import NaanFactory

class RunFactory(NaanFactory):

    def __init__(self):
        super().__init__()


    def run_factory(self):
        if (super().make_dough() == "dough") and (super().bake_dough() == "naan"):
            return "Here's your naan"
        else:
            return False