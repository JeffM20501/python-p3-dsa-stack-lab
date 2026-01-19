class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit
    
    def __str__(self):
        return f'items={self.items}, limit={self.limit}'

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if len(self.items):
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items)>=self.limit

    def search(self, target):
        if target not in self.items:
            return -1
        index = self.items.index(target)
        return len(self.items) - 1 - index
