class HashTable:

    def __init__(self, hash_function, size_hash_table) -> None:
        self.__hash_function = hash_function
        self.__hash_table = [[] for _ in range(size_hash_table)]

    def insert(self, key, value):
        hash_key  = self.__hash_function(key)
        bucket = self.__hash_table[hash_key]
        key_exists = False

        for index, keyvalue in enumerate(bucket):
            key_pair, value_pair = keyvalue

            if key_pair == key:
                key_exists = True
                break
            
        if key_exists:
            bucket[index] = (key, value)
            return
        
        bucket.append((key, value))

    def __str__(self):
        return str(self.__hash_table)


def create_hashing_func(size):
    return lambda key: key % size


hash_table = HashTable(create_hashing_func(5), 5)
hash_table.insert(3, 'John')
hash_table.insert(18, 'John2')
print(hash_table)
#[[], [], [], [(3, 'John'), (18, 'John2')], []]
