import unittest

from components.box import Box
from components.load import Load


class TestBox(unittest.TestCase):

    def test_create_box(self):
        box1 = Box()
        self.assertNotEqual(box1.get_id(), None)

    def test_create_box_with_parent(self):
        box1 = Box()
        box2 = Box(box1)
        self.assertEqual(box2.get_parent(), box1)

    def test_boxes_different_ids(self):
        box1 = Box()
        box2 = Box()
        self.assertNotEqual(box1.get_id(), box2.get_id())

    def test_link_boxes(self):
        box1 = Box()
        box2 = Box()
        box1.set_parent(box2)
        self.assertEqual(box1.get_parent(), box2)
        self.assertEqual(box2.get_children()[0], box1)

    def test_link_multiple_boxes(self):
        boxm1 = Box()
        boxh1 = Box()
        boxh2 = Box()
        boxh1.set_parent(boxm1)
        boxh2.set_parent(boxm1)
        self.assertEqual(boxm1.get_children()[0], boxh1)
        self.assertEqual(boxm1.get_children()[1], boxh2)

    def test_no_parent_child_loop(self):
        box1 = Box()
        box2 = Box()
        box1.set_parent(box2)
        box2.set_parent(box1)
        self.assertEqual(box1.get_children()[0], box2)
        self.assertEqual(box2.get_parent(), box1)
        self.assertEqual(box2.get_children(), [])
        self.assertNotEqual(box1.get_parent(), box2)

    def test_no_long_loops(self):
        box1 = Box()
        box2 = Box()
        box3 = Box()
        box3.set_parent(box2)
        box2.set_parent(box1)
        box1.set_parent(box3)
        self.assertEqual(box3.get_parent(), None)
        self.assertEqual(box2.get_children(), [])
        self.assertEqual(box1.get_parent(), box3)

    def test_no_self_loop(self):
        box1 = Box()
        with self.assertRaises(ValueError):
            box1.set_parent(box1)
        self.assertEqual(box1.get_children(), [])
        self.assertEqual(box1.get_parent(), None)

    def test_give_child_a_child(self):
        box1 = Box()
        box2 = Box()
        box3 = Box()
        box3.set_parent(box1)
        box2.set_parent(box1)
        # 1 tiene children [2,3]
        box3.set_parent(box2)
        self.assertEqual(box3.get_parent(), box2)
        self.assertEqual(len(box1.get_children()), 1)
        self.assertEqual(box1.get_children(), [box2])
        self.assertEqual(box2.get_children(), [box3])

    def test_add_load(self):
        box1 = Box()
        load1 = Load("Uno")
        box1.add_load(load1)
        self.assertEqual(box1.get_loads(), [load1])

    def test_add_multiple_loads(self):
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos")
        box1.add_load(load1)
        box1.add_load(load2)
        self.assertEqual(box1.get_loads(), [load1, load2])

    def test_delete_load(self):
        box1 = Box()
        load1 = Load("Uno")
        box1.add_load(load1)
        box1.delete_load(load1)
        self.assertEqual(box1.get_loads(), [])

    def test_delete_only_chosen_load(self):
        box1 = Box()
        load1 = Load("Uno")
        load2 = Load("Dos")
        box1.add_load(load1)
        box1.add_load(load2)
        box1.delete_load(load2)
        self.assertEqual(box1.get_loads(), [load1])

    def test_box_with_defined_loads(self):
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos", 200)
        box1.add_load(load1)
        box1.add_load(load2)
        self.assertEqual(box1.defined(), True)

    def test_box_with_undefined_loads(self):
        box1 = Box()
        load1 = Load("Uno", 100)
        load2 = Load("Dos")
        box1.add_load(load1)
        box1.add_load(load2)
        self.assertEqual(box1.defined(), False)

    def test_box_with_defined_children(self):
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

    def test_box_with_undefined_children(self):
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


if __name__ == '__main__':
    unittest.main()
