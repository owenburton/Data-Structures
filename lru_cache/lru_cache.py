from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit 
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = {}
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        try:
            # move k,v pair so considered most-recent
            self.dll.move_to_front(self.storage[key])
            return (self.storage[key]).value
        except KeyError:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # size_before = self.dll.length

        try:
            node = self.storage[key]
            self.dll.move_to_front(node)
            self.dll.head.value = value
            self.storage[key] = self.dll.head
        except KeyError:
            self.dll.add_to_head(value)
            self.storage[key] = self.dll.head

        # if over limit, remove oldest
        if self.dll.length > self.limit:
            deleted = self.dll.remove_from_tail()
            for k,v in self.storage.items():
                if v==deleted:
                    self.storage.pop(k)
                    break

    
    def print_dll(self):
        current = self.dll.head 
        out = []
        while current:
            out.append(current.value)
            current = current.next
        return ','.join(out)
         
        

