class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev

        nxt.prev = node
        node.next = nxt
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            self.insert(node) # recently gotten so front of dll
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        
        node = ListNode(key, value)
        self.lookup[key] = node
        self.insert(node)

        if len(self.lookup) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.lookup[lru.key]
