import unittest
from core_lld import LinkedList

class LinkedListTest(unittest.TestCase):

    # def test_init(self):
    #     # Create a new linked list
    #     linked_list = LinkedList(11)

    #     # Assert that the linked list is empty
    #     self.assertEqual(linked_list.size(), 1)

    def test_add(self):
        # Create a new linked list
        linked_list = LinkedList(1)

        # Add a new node to the linked list
        linked_list.append(2)

        # Assert that the linked list is not empty
        linked_list.print_list()

        # self.assertEqual(linked_list.print_list(), 1,2)

        # Assert that the value of the first node is 1
        # self.assertEqual(linked_list.get(0), 1)

    def test_remove(self):
        # Create a new linked list
        linked_list = LinkedList(1)

        # Add a new node to the linked list
        # linked_list.add(2)

        # Remove the first node from the linked list
        linked_list.pop()

        # Assert that the linked list is empty
        self.assertEqual(linked_list.print_list(), 0)

if __name__ == '__main__':
    unittest.main()