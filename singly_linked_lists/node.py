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

    def delete_node(self, key):
        # 1. case of deleting head node
        # Assume head node is Node_A
        # self.head points to Node_A
        # current_node points to Node_A
        current_node = self.head
        # if a head node exists (not None) and its data property matches the key
        if current_node and current_node.data == key:
            # self.head points to Node_B
            self.head = current_node.next
            # current_node points to None
            # So no variables point to Node_A any more, which is then deleted
            current_node = None
            return
        # 2. case of deleting node other than the head
        prev_node = None  # optional, prev_node can be init within the while loop as well
        # Assume deleting Node_B
        # while current_node is to check if we are already at the end of the linked list
        while current_node and current_node.data != key:
            prev_node = current_node  # prev_node == Node_A when while loop terminated
            # current_node == Node_B when while loop terminated
            current_node = current_node.next
        # for the case that we are at the end of the linked list but still can't find the node with key
        if current_node is None:
            return
        # Node_A.next needs to point to Node_C
        prev_node.next = current_node.next
        # delete Node_B
        current_node = None

    def delete_node_at_pos(self, index):
        current_node = self.head
        # 1. delete the head node
        if current_node and index == 0:
            self.head = current_node.next
            current_node = None
            return

        # 2. delete according to index
        current_index = 0
        prev_node = None
        while current_index != index and current_node:
            prev_node = current_node
            current_node = current_node.next
            current_index += 1

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    def len_iterative(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    # init call have to pass the head node as argument so that it can traverse by calling node.next
    # no need to init a count variable because the return statement aggregate cumulative result from recursive calls
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


llist = LinkedList()
print("The length of an empty linked list is:")
print(llist.len_recursive(llist.head))
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("The length of the linked list calculated recursively after inserting 4 elements is:")
print(llist.len_recursive(llist.head))
print("The length of the linked list calculated iteratively after inserting 4 elements is:")
print(llist.len_iterative())
