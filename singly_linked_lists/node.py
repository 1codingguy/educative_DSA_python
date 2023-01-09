class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # None in Python is null, which marks the end of a linked list


class LinkedList:
    def __init__(self):
        # when constructor is invoked, head is None (null) to signify it's the last node?
        self.head = None

    def print_list(self):
        # starts from the head, which is a Node object
        current_node = self.head
        while current_node:
            print(current_node.data)
            # this will point to the next Node object
            # remember for the last node, Node.next == None, which will terminate the while loop
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)  # to create a new node
        # 1. Empty linked list case
        if self.head == None:
            self.head = new_node
            return
        # 2. Non-empty linked list case, traverse the entire linked list
        last_node = self.head
        # if the node has a truthy value in .next property (non None)
        while last_node.next:
            # the last_node should be the node+1 position
            # which loops until we see a node with self.next == None, which means the last node
            last_node = last_node.next
        # assign the new_node as the last_node
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        # the next of the new node should point to the current head
        new_node.next = self.head
        # assign the new_node as the new head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        # case when prev_node == None
        if not prev_node:
            print("Previous node doesn't exist")
            return
        # create a new node
        new_node = Node(data)
        # point the new Node.next to the prev_node.next
        new_node.next = prev_node.next
        # update prev_node.next, to point to the new node
        prev_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")


llist.insert_after_node(llist.head.next, "D")

llist.print_list()
