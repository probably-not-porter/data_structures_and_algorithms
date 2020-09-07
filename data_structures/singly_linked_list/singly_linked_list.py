# Singly-Linked List 
# Python
# Porter L

class Node:
    """ Class for a single node """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # Methods

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    """ Singly Linked List class """

    def __init__(self, head=None):
        self.head = head

    # Methods
    
    def insert(self, data):
        """ Adds a new node as the head of the list, pushing everything else by 1 """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """ Return length of the list by counting nodes """
        target = self.head
        count = 0
        while target:
            count += 1
            target = target.get_next()
        return count
    
    def search(self, data):
        """ Search for a specific data value in the list """
        target = self.head
        found = False
        while target and found is False:
            if target.get_data() == data:
                found = True
            else:
                target = target.get_next()
        if target is None:
            raise ValueError("Node containing " + str(data) + " could not be found.")
        return target

    def delete(self, data):
        """ Remove a node by its data value from the list """
        target = self.head
        previous = None
        found = False
        while target and found is False:
            if target.get_data() == data:
                found = True
            else:
                previous = target
                target = target.get_next()
        if target is None:
            raise ValueError("Node containing " + str(data) + " could not be found.")
        if previous is None:
            self.head = target.get_next()
        else:
            previous.set_next(target.get_next())


# Example
if __name__=='__main__': 
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    print(list.size()) # shoudl be 3
    list.search(2)
    #list.delete(4) # should be valueerror
    list.delete(2) # should not be valueerror
    print(list.size()) # should be 2