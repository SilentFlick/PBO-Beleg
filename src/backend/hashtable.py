class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hash_function(self, key):
        hex_key = key.encode().hex()
        hash_index = int(hex_key, 16) % self.size
        return hash_index

    def put(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def get(self, key):
        index = self.hash_function(key)
        for k in self.table[index]:
            if k == key:
                return True
        return False

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index].remove(key)
