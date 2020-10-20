"""
Your task is create your own HashTable without using a built-in library.
​
Your HashTable needs to have the following functions:
​
- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
​
Example:
​
```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None
​
class MyHashTable:
    def __init__(self, capacity=10):
        # Your code here
        # hash tables use an array for storage 
        self.storage = [None] * capacity
        # self.storage = [None for _ in range(capacity)]
        self.num_items = 0
        self.capacity = capacity
        self.threshold = 0.75
​
    # O(k) where k is the size of the key 
    def _hash(self, key):
        """
        DJB2 hash, 32-bit
        """
        # Cast the key to a string and get bytes
        str_key = str(key).encode()
​
        # Start from an arbitrary large prime
        hash_value = 5381
​
        # Bit-shift and sum value for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits
​
        # we need to ensure that this output is actually in bounds of our array 
        print("hash value before %: ", hash_value)
​
        return hash_value % self.capacity
​
    def _get_load_factor(self):
        return self.num_items / self.capacity
​
    def _resize(self):
        # 1. Check if the load factor of our storage array >= threshold 
        if self._get_load_factor() >= self.threshold:
            # 2. If we determine that we need to resize, init a new storage 
            # array with twice the capacity 
            self.capacity *= 2
            old_storage = self.storage
            self.storage = [None] * self.capacity
            # 3. Iterate through every key-value pair and re-index it into 
            # our new storage array 
            for node in old_storage:
                current = node 
                while current:
                    self.put(current.key, current.value)
                    current = current.next
​
    def put(self, key, value):
        # Your code here
        self._resize()
        # 1. run our key through our hash function to get the index 
        index = self._hash(key) # O(k)
        print("Put index: ", index)
        # 2. set the key and value in the array at that index 
        # check if the slot is occupied or not 
        if self.storage[index] is None:
            self.storage[index] = LLNode(key, value)
        else:
            current = self.storage[index]
            # traverse through our LL until we get to the last LL node 
            while current.next is not None:
                # we need to check if any of the LL nodes have the key 
                # we're looking to insert 
                if current.key == key:
                    current.value = value 
                current = current.next 
            
            # check the tail to see if we need to overwrite its value
            if current.key == key:
                current.value = value 
​
            current.next = LLNode(key, value)
        
        self.num_items += 1
​
        # self.storage[index] = (key, value) # O(1)
        # print(self.storage)
​
    def get(self, key):
        # Your code here
        # 1. run our key through our hash function to get the index 
        index = self._hash(key) # O(k)
        print("Get index: ", index)
        # 2. access the key-value pair at the index in our array and return 
        # just the value, which is the second element of the key-value tuple
        print(self.storage)
​
        # handle the case where the key-value pair is not in our hash table 
        # if self.storage[index] is None:
        #     return None
​
        current = self.storage[index]
​
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next 
​
        # if we've traversed through the entire LL and didn't find the kv pair,
        # return None 
        return None
​
    def remove(self, key):
        # Your code here
        # 1. run our key through our hash function to get the index 
        index = self._hash(key) # O(k)
        print("Get index: ", index)
        # 2. access the key-value pair at the index in our array 
        # set that spot to None 
        print(self.storage)
​
        prev = self.storage[index]
        current = prev.next 
​
        while current:
            if current.key == key:
                prev.next = current.next
                break
            current = current.next 
            prev = prev.next 
        
        self.num_items -= 1
​
        # self.storage[index] = None # O(1)
​
​
ht = MyHashTable()
print(ht.storage)
​
ht.put("a", "b")
ht.put("cow", "llama")
​
ht.put("cat", "dog")
ht.put("fish", "bird")
print(ht.get("cat"))
print(ht.get("cow"))
ht.put("i", "j")
