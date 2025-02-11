"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.""" 
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        
        #  check for the head & tail if they dont exist do something
        if not self.head and not self.tail:
            # Set head & tail to new nodes
            self.head = new_node
            self.tail = new_node
        else:
            #  swap pointers before we over write data
            self.head.prev = new_node
            self.head = new_node
        
        # increment the length
        self.length += 1



    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #  Capture the value because we cant get it once its deleted
        value = self.head.value
        #  Detetes the head
        self.delete(self.head)
        #  Returns the value of the head (thats now deleted)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            #  swap pointers before we over write data
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #  If we are at the front of the list we do this
        if node is self.head:
            #  We just return
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        #  If we are at the end of the list do this
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    #  Note: Nodes can delete themselves, this handles the metadata
    def delete(self, node):
        self.length -= 1

        #  If the head is the tail its the only node
        if self.head is self.tail:
            #  Get rid of it
            self.head = None
            self.tail = None
        #  If the node is the head do this
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        #  If the node is the tail do this
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        # If none of these are true, just delete
        else:
            node.delete()

            
    """Returns the highest value currently in the list"""
    def get_max(self):
        #  If its empty, theres no max
        if not self.head:
            return None
        
        max_val = self.head.value
        current = self.head

        #  Iterates through the list from head -> tail
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

