# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # Hash key to get insertion index
        index = self._hash_mod(key)

        # Created linked pair from key,value and reassign value to linked pair
        value = LinkedPair(key, value)

        # insert value into bucket
        if self.storage[index] is None:
            self.storage[index] = value
        else:
            value.next = self.storage[index]
            self.storage[index] = value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Hash key to get removal index
        index = self._hash_mod(key)

        # Check if bucket is empty
        if self.storage[index] is None:
            return None

        # Store refrence to current pair
        current_pair = self.storage[index]

        # Loop through all pairs in bucket
        while current_pair:
            # Remove pair if key matches
            if current_pair.key == key:
                self.storage[index] = current_pair.next

            current_pair = current_pair.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Hash key to get retrieval index
        index = self._hash_mod(key)

        # Create bucket reference
        bucket = self.storage[index]

        # Check if bucket is empty
        if bucket is None:
            return None

        while bucket:
            # Check if keys match
            if bucket.key == key:
                # Return value
                return bucket.value

            # Reassign current bucket
            bucket = bucket.next

        # Return none if key isn't found
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        # Create ref of original storage
        temp_storage = self.storage

        # Double capacity
        self.capacity = self.capacity * 2

        # Resize current storage
        self.storage = [None] * self.capacity

        # Copy pairs into new storage
        for i in range(self.capacity // 2):
            # Hash current value in bucket if there aren't any descendants
            if temp_storage[i] and temp_storage[i].next is None:
                self.insert(temp_storage[i].key, temp_storage[i].value)
            else:
                # Hash descendants in current bucket
                while temp_storage[i]:
                    self.insert(temp_storage[i].key, temp_storage[i].value)
                    temp_storage[i] = temp_storage[i].next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
