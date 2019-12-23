import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#  A stack is first in -> last out.

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        #  If the size is bigger than 0 do something
        if self.size > 0:
            #  remove from tail & decrement self by 1
            popper = self.storage.remove_from_tail()
            self.size -= 1
            return popper
        else:
            return None

    def len(self):
        return self.size
