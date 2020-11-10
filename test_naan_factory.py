from run_factory import RunFactory
import unittest
import pytest

class TestNaanFactory(unittest.TestCase):

    test_run = RunFactory()

    def test_make_dough(self):
        self.assertEqual(self.test_run.make_dough(), "dough")

    def test_bake_dough(self):
        if self.assertEqual(self.test_run.make_dough(), "dough"):
            self.assertEqual(self.test_run.bake_dough(), "naan")
        else:
            return False

    def test_run_factory(self):
        if (self.assertEqual(self.test_run.make_dough(), "dough")) and (self.assertEqual(self.test_run.bake_dough(), "naan")):
            self.assertEqual(self.test_run.run_factory(), "Here's your naan")
        else:
            return False
