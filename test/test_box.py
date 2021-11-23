import unittest

from components.box import Box
from components.load import Load


class TestBoxCreateMethods(unittest.TestCase):
    def test_when_create_box_then_id_is_not_none(self):
        box1 = Box()
        self.assertNotEqual(box1.get_id(), None)

    def test_when_create_box_with_parent_then_parent_is_set(self):
        box1 = Box()
        box2 = Box(box1)
        self.assertEqual(box2.get_parent(), box1)

    def test_when_creating_multiple_boxes_then_boxes_have_different_ids(self):
        box1 = Box()
        box2 = Box()
        self.assertNotEqual(box1.get_id(), box2.get_id())


class TestBoxChildMethods(unittest.TestCase):
    def test_when_set_parent_to_box2_then_box2_becomes_parent(self):
        box1 = Box()
        box2 = Box()
        box1.set_parent(box2)
        self.assertEqual(box1.get_parent(), box2)

    def test_when_set_parent_to_box2_then_box1_becomes_child_of_box2(self):
        box1 = Box()
        box2 = Box()
        box1.set_parent(box2)
        self.assertEqual(box2.get_children()[0], box1)

    def test_when_giving_few_children_then_box_has_few_children(self):
        boxm1 = Box()
        boxh1 = Box()
        boxh2 = Box()
        boxh1.set_parent(boxm1)
        boxh2.set_parent(boxm1)
        self.assertEqual(boxm1.get_children(), [boxh1, boxh2])

    def test_when_set_parent_to_self_then_raises_error(self):
        box1 = Box()
        with self.assertRaises(ValueError):
            box1.set_parent(box1)

    def test_when_setting_parent_to_child_then_loop_is_broken(self):
        box1 = Box()
        box2 = Box()
        box1.set_parent(box2)
        box2.set_parent(box1)
        self.assertNotEqual(box1.get_parent(), box2)

    def test_when_setting_parent_to_descendant_then_loop_is_broken(self):
        box1 = Box()
        box2 = Box()
        box3 = Box()
        box3.set_parent(box2)
        box2.set_parent(box1)
        box1.set_parent(box3)
        self.assertEqual(box3.get_parent(), None)

    def test_when_removing_parent_then_child_looses_parent(self):
        box1 = Box()
        box2 = Box(box1)
        box2.set_parent(None)
        self.assertEqual(box2.get_parent(), None)

    def test_when_removing_parent_then_parent_looses_child(self):
        box1 = Box()
        box2 = Box(box1)
        box2.set_parent(None)
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
        box1.set_parent(box0)
        box2.set_parent(box0)
        self.assertEqual(box0.defined(), True)

    def test_when_undefined_children_and_no_loads_then_it_is_undefined(self):
        box0 = Box()
        box1 = Box()
        box2 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos")
        box1.add_load(load1)
        box2.add_load(load2)
        box1.set_parent(box0)
        box2.set_parent(box0)
        self.assertEqual(box0.defined(), False)

    def test_when_defined_children_and_loads_then_defined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box0.add_load(load2)
        box1.set_parent(box0)
        self.assertEqual(box0.defined(), True)

    def test_when_undefined_children_and_defined_loads_then_undefined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box0.add_load(load2)
        box1.set_parent(box0)
        self.assertEqual(box0.defined(), False)

    def test_when_defined_children_and_undefined_loads_then_undefined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos")
        box1.add_load(load1)
        box0.add_load(load2)
        box1.set_parent(box0)
        self.assertEqual(box0.defined(), False)

    def test_when_undefined_children_and_undefined_loads_then_undefined(self):
        box0 = Box()
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos")
        box1.add_load(load1)
        box0.add_load(load2)
        box1.set_parent(box0)
        self.assertEqual(box0.defined(), False)


if __name__ == '__main__':
    unittest.main()
