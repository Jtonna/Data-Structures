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
        #  If the size is zero, we just return, else
        if self.size == 0:
            return
        else:
            self.size -= 1
            #  We need to store the value elsewhere to prevent it from being modified by +1 so we can return it later
            head_true_value = self.storage.head.value
            self.storage.remove_from_head()
            return head_true_value

    def len(self):
        return self.size
