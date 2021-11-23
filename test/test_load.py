import unittest

from components.load import Load


class TestLoadConstructor(unittest.TestCase):
    def test_when_create_load_then_name_is_set(self):
        load0 = Load("Zero")
        self.assertEqual(load0.name, "Zero")

    def test_when_create_load_without_power_then_power_is_None(self):
        load0 = Load("Zero")
        self.assertIsNone(load0.power)

    def test_when_create_load_with_power_then_power_is_set(self):
        load0 = Load("Zero", 100)
        self.assertEqual(load0.power, 100)

    def test_when_create_load_with_negative_power_then_power_is_ignored(self):
        load0 = Load("Zero", -100)
        self.assertEqual(load0.power, None)


class TestLoadSetterMethods(unittest.TestCase):
    def test_when_set_positive_power_then_power_assigned(self):
        load0 = Load("Zero")
        load0.power = 100
        self.assertEqual(load0.power, 100)

    def test_when_set_negative_power_then_power_ignored(self):
        load0 = Load("Zero")
        load0.power = -100
        self.assertEqual(load0.power, None)

    def test_when_set_name_then_new_name_assigned(self):
        load0 = Load("Prince")
        load0.name = "The load previously known as Prince"
        self.assertEqual(load0.name,
                         "The load previously known as Prince")


class TestLoadDefinedMethod(unittest.TestCase):
    def test_when_power_is_positive_then_defined(self):
        load0 = Load("Zero", 100)
        self.assertEqual(load0.defined(), True)

    def test_when_power_is_undefined_then_undefined(self):
        load0 = Load("Zero")
        self.assertEqual(load0.defined(), False)

    def test_when_power_is_given_afterwards_and_positive_then_defined(self):
        load0 = Load("Zero")
        load0.power = 2
        self.assertEqual(load0.defined(), True)


if __name__ == '__main__':
    unittest.main()
