from run_factory import RunFactory # inherits from RunFactory class
# importing unittest and pytest modules for testing
import unittest
import pytest

# class with test cases for the functions of the NaanFactory and RunFactory classes
class TestNaanFactory(unittest.TestCase):

    test_run = RunFactory() # an instance of the Runfactory class, which inherits from NaanFactory

    # function testing make_dough() function
    def test_make_dough(self):
        self.assertEqual(self.test_run.make_dough(), "dough")
        # Boolean: if make_dough() returns "dough" (when user inputs water and flour as ingredients), returns True and passes

    # function testing bake_dough() function
    def test_bake_dough(self):
        # if make_dough() returns dough, bake_dough() should return naan
        if self.assertEqual(self.test_run.make_dough(), "dough"):
            self.assertEqual(self.test_run.bake_dough(), "naan")
            # Boolean: if bake_dough() returns naan when make_dough() returns dough, returns True and passes
        else:
            return False # if make_dough() doesn't return dough, bake_dough should return false to pass

    # function testing run_factory() function
    def test_run_factory(self):
        # if bake_dough() returns naan, should return a message informing the user
        if self.assertEqual(self.test_run.bake_dough(), "naan"):
            self.assertEqual(self.test_run.run_factory(), "Here's your naan")
            # Boolean: if run_factory() returns a message informing user when bake_dough returns naan, returns True and passes
        else:
            return False # if bake_dough() doesn't return naan, run_factory should return false to pass
