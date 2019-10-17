import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#  A queue is first in -> first out.

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #  Since were adding an item to the queue we need to add one
        self.size += 1

        #  If the storage.head is Null do something, if not -> else
        if self.storage.head is None:
            #  We add the value to the head
            self.storage.add_to_head(value)
        else:
            #  Add it to the tail
            self.storage.add_to_tail(value)

    def dequeue(self):
        #  If the size is zero do something
        if self.size == 0:
            pass

    def len(self):
        pass
