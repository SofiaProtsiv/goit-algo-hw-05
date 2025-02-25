class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        for i in range(len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
        return False

    def __contains__(self, key):
        return self.get(key) is not None

    def __str__(self):
        items = []
        for bucket in self.table:
            for pair in bucket:
                items.append(f"{pair[0]}: {pair[1]}")
        return "\n".join(items)

H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Вся таблиця до видалення елемента:\n", H)
print(H.get("apple"))
print(H.get("orange"))
print(H.get("banana"))

H.delete("orange")

print("Вся таблиця після видалення елемента:\n", H)
print(H.get("orange"))
