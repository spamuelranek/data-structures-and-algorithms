from linked_list.linked_list import LinkedList

class LinkedListHashTable(LinkedList):
    def includes(self, key, definition_in_hash):
        current = self.head

        while current:
            keys = current.value.keys()
            for testing_key in keys:
                if testing_key == key:
                    if definition_in_hash == "get":
                        return current.value[key]
                    if definition_in_hash == "contains":
                        return True
            current = current.next

        if definition_in_hash == "get":
            return "null"
        if definition_in_hash == "contains":
            return False

class HashTable:

    def __init__(self, number_of_buckets):
        self.buckets = [None for _ in range(0,number_of_buckets) ]

    def hash(self,string):
        total_ascii_value = 0
        for char in string:
            total_ascii_value = total_ascii_value + ord(char)
        index_hash = total_ascii_value % len(self.buckets)
        return index_hash

    def add(self,key,value):
        hash_index = self.hash(key)

        if self.buckets[hash_index] is None:
            hashed_item = LinkedListHashTable()
            hashed_item.append({key:value})
            self.buckets[hash_index] = hashed_item

        else:
            self.buckets[hash_index].append({key:value})


    def list_includes(self,key,definition):
        hash_index = self.hash(key)
        value = False
        if self.buckets[hash_index] is not None:
            value = self.buckets[hash_index].includes(key,definition)
        return value



    def contains(self,key):
        return self.list_includes(key,"contains")

    def get(self,key):
        return self.list_includes(key, "get")





