class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]

    def __repr__(self) -> str:
        return str(self.items)