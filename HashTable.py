class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize buckets for separate chaining

    def _hash(self, key):
        return hash(key) % self.size  # Compute index from key

    def insert(self, key, value):
        index = self._hash(key)
        # Check if key exists and update if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If key doesn't exist, append new (key, value) pair
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        # Search for key in the appropriate bucket
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        # Locate and remove key from the bucket
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False  # Key not found
