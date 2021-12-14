class HashTable:

    def __init__(self, hash_function, size_hash_table) -> None:
        self.__hash_function = hash_function
        self.__hash_table = [None] * size_hash_table

    def insert(self, key, value):
        hash_key  = self.__hash_function(key)
        self.__hash_table[hash_key] = value

    def __str__(self):
        return str(self.__hash_table)


def create_hashing_func(size):
    return lambda key: key % size


hash_table = HashTable(create_hashing_func(5), 5)
hash_table.insert(3, 'John')
print(hash_table)
#[None, None, None, 'John', None]
