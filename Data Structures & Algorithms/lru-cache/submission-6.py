class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.lookup = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.tail.next = self.head
        self.head.prev = self.tail
    
    def insert(self, node):
        prev, next = self.head.prev, self.head
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None: # IMPORTANT ONE TO LEARN
        if key in self.lookup:
            self.remove(self.lookup[key])

        node = Node(key, value)
        self.lookup[key] = node
        self.insert(node)

        if len(self.lookup) > self.size:
            lru = self.tail.next
            self.remove(lru)
            del self.lookup[lru.key]



