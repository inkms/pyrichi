import unittest

from components.box import Box
from components.load import Load


class TestBoxCreateMethods(unittest.TestCase):
    def test_when_create_box_then_id_is_not_none(self):
        box1 = Box()
        self.assertNotEqual(box1.get_id(), None)

    def test_when_creating_multiple_boxes_then_boxes_have_different_ids(self):
        box1 = Box()
        box2 = Box()
        self.assertNotEqual(box1.get_id(), box2.get_id())


class TestBoxChildMethods(unittest.TestCase):
    def test_when_add_child_then_box_becomes_parent(self):
        box1 = Box()
        box2 = Box()
        box1.add_child(box2)
        self.assertEqual(box2.get_parent(), box1)

    def test_when_add_box2_to_1_then_box2_becomes_child_of_box1(self):
        box1 = Box()
        box2 = Box()
        box1.add_child(box2)
        self.assertEqual(box1.get_children(), [box2])

    def test_when_giving_few_children_then_box_has_few_children(self):
        box_m1 = Box()
        box_h1 = Box()
        box_h2 = Box()
        box_m1.add_child(box_h1)
        box_m1.add_child(box_h2)
        self.assertEqual(box_m1.get_children(), [box_h1, box_h2])

    def test_when_add_self_as_child_then_raises_error(self):
        box1 = Box()
        with self.assertRaises(ValueError):
            box1.add_child(box1)

    def test_when_adding_parent_as_child_then_raises_error(self):
        box1 = Box()
        box2 = Box()
        box1.add_child(box2)
        with self.assertRaises(ValueError):
            box2.add_child(box1)

    def test_when_adding_ascendant_as_child_then_raises_error(self):
        box1 = Box()
        box2 = Box()
        box3 = Box()
        box1.add_child(box2)
        box2.add_child(box3)
        with self.assertRaises(ValueError):
            box3.add_child(box1)

    def test_when_removing_parent_then_parent_looses_child(self):
        box1 = Box()
        box2 = Box()
        box1.add_child(box2)
        box1.delete_child(box2)
        self.assertEqual(box1.get_children(), [])


class TestBoxLoadMethods(unittest.TestCase):
    def test_when_add_load_then_get_load_shows_load(self):
        box1 = Box()
        load1 = Load("Uno")
        box1.add_load(load1)
        self.assertEqual(box1.get_loads(), [load1])

    def test_when_add_multiple_loads_then_get_load_shows_multiple_loads(self):
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos")
        box1.add_load(load1)
        box1.add_load(load2)
        self.assertEqual(box1.get_loads(), [load1, load2])

    def test_when_delete_load_then_load_is_removed(self):
        box1 = Box()
        load1 = Load("Uno")
        box1.add_load(load1)
        box1.delete_load(load1)
        self.assertEqual(box1.get_loads(), [])

    def test_when_few_loads_and_delete_one_then_only_chosen_load_is_gone(self):
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos")
        box1.add_load(load1)
        box1.add_load(load2)
        box1.delete_load(load2)
        self.assertEqual(box1.get_loads(), [load1])


class TestBoxDefinedMethod(unittest.TestCase):
    def test_when_box_has_defined_loads_then_it_is_defined(self):
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box1.add_load(load2)
        self.assertEqual(box1.defined(), True)

    def test_when_box_has_undefined_loads_then_it_is_undefined(self):
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos")
        box1.add_load(load1)
        box1.add_load(load2)
        self.assertEqual(box1.defined(), False)

    def test_when_defined_children_and_no_loads_then_it_is_defined(self):
        box0 = Box()
        box1 = Box()
        box2 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box2.add_load(load2)
        box0.add_child(box1)
        box0.add_child(box2)
        self.assertEqual(box0.defined(), True)

    def test_when_undefined_children_and_no_loads_then_it_is_undefined(self):
        box0 = Box()
        box1 = Box()
        box2 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos")
        box1.add_load(load1)
        box2.add_load(load2)
        box0.add_child(box1)
        box0.add_child(box2)
        self.assertEqual(box0.defined(), False)

    def test_when_defined_children_and_loads_then_defined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box0.add_load(load2)
        box0.add_child(box1)
        self.assertEqual(box0.defined(), True)

    def test_when_undefined_children_and_defined_loads_then_undefined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box0.add_load(load2)
        box0.add_child(box1)
        self.assertEqual(box0.defined(), False)

    def test_when_defined_children_and_undefined_loads_then_undefined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos")
        box1.add_load(load1)
        box0.add_load(load2)
        box0.add_child(box1)
        self.assertEqual(box0.defined(), False)

    def test_when_undefined_children_and_undefined_loads_then_undefined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos")
        box1.add_load(load1)
        box0.add_load(load2)
        box0.add_child(box1)
        self.assertEqual(box0.defined(), False)


class TestBoxDelete(unittest.TestCase):

    def test_when_deleting_box_then_reference_lost(self):
        box = Box()
        del box
        with self.assertRaises(UnboundLocalError):
            # noinspection PyUnboundLocalVariable
            box.get_id()

    # def test_when_deleting_box_then_children_lost(self):
    #     box1 = Box()
    #     box2 = Box()
    #     box1.add_child(box2)
    #     del box1
    #     with self.assertRaises(UnboundLocalError):
    #         box2.get_id()


if __name__ == '__main__':
    unittest.main()
