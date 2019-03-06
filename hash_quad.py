# CPE 202 Project 4 
# Name: Ashley Sutter
# Student ID: 011278952
# Date (last modified): 3/4/2019
#
# Project 4
# Section 5
# Purpose of Lab: Create a concordance list of an input file using a hash table
# additional comments

class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        index = self.horner_hash(key)
        self.insert_helper(key, value, index, 1)
        if self.get_load_factor() > 0.5:
            old_hash_table = self.hash_table
            self.__init__(self.table_size * 2 + 1)
            for i in range(len(old_hash_table)):
                item = old_hash_table[i]
                if item != None:
                    key = item[0]
                    values = item[1]
                    for value in values:
                        self.insert(key, value)

    def insert_helper(self, key, value, index, n):
        #does not test if quadratic probing doesn't hit a None
        if self.hash_table[index] == None: #basecase
            self.hash_table[index] = [key, [value]]
            self.num_items += 1
            return
        elif self.hash_table[index][0] == key:
            self.hash_table[index][1].append(value)
            return
        index = (index + pow(n, 2)) % self.table_size
        return self.insert_helper(key, value, index, n+1)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        answer = 0
        n = min(len(key), 8)
        for i in range(len(key)):
            answer += ord(key[i]) * pow(31, (n - 1 - i), self.table_size)
        answer = answer % self.table_size
        return answer

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        if self.get_value(key) == None:
            return False
        return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        index = self.horner_hash(key)
        return self.get_index_helper(key, index, 1)

    def get_index_helper(self, key, index, n):
        if self.hash_table[index] == None:
            return None
        elif self.hash_table[index][0] == key:
            return index
        index = (index + pow(n, 2)) % self.table_size
        return self.get_index_helper(key, index, n+1)

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        all_keys = []
        for i in range(self.table_size):
            if self.hash_table[i] != None:
                all_keys.append(self.hash_table[i][0])
        return all_keys

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        index = self.get_index(key)
        if index == None:
            return None
        return self.hash_table[index][1]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
