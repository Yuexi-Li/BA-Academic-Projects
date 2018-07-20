"""This HashTable class stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self._len=0
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        value=self.calculate_hash_value(string)
        hv=self.lookup(string)
        if hv !=-1:
            if string in self.table[value]:
                return 
            else:
                self._len+=1
                self.table[value].append(string)
                return 
        else:
            self._len+=1
            self.table[value]= [string]
            return 
            
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hv=self.calculate_hash_value(string)
        if self.table[hv]==None: 
            return -1 
        else:
            if string in self.table[hv]:
                return hv

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string. Assume this string will at least 2"""
        value=ord(string[0])*100+ord(string[1])
        return value
        
    def __len__(self):
        return self._len

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
hash_table.store('UXACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
print len(hash_table)

