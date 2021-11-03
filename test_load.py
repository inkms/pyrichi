import unittest

from components.load import Load


class TestLoad(unittest.TestCase):

    def test_create_load(self):
        load0 = Load("Zero")
        self.assertEqual(load0.get_name(), "Zero")
        self.assertEqual(load0.get_power(), None)

    def test_create_load_with_power(self):
        load0 = Load("Zero", 100)
        self.assertEqual(load0.get_power(), 100)

    def test_create_load_with_negative_power(self):
        load0 = Load("Zero", -100)
        self.assertEqual(load0.get_power(), None)

    def test_set_power(self):
        load0 = Load("Zero")
        load0.set_power(100)
        self.assertEqual(load0.get_power(), 100)

    def test_set_negative_power(self):
        load0 = Load("Zero")
        load0.set_power(-100)
        self.assertEqual(load0.get_power(), None)

    def test_change_name(self):
        load0 = Load("Prince")
        load0.set_name("The load previously known as Prince")
        self.assertEqual(load0.get_name(),
                         "The load previously known as Prince")

    def test_defined_when_defined(self):
        load0 = Load("Zero", 100)
        self.assertEqual(load0.defined(), True)

    def test_defined_when_undefined(self):
        load0 = Load("Zero")
        self.assertEqual(load0.defined(), False)

    def test_defined_if_defining_afterwards(self):
        load0 = Load("Zero")
        load0.set_power(2)
        self.assertEqual(load0.defined(), True)


if __name__ == '__main__':
    unittest.main()
