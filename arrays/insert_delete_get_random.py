import random

class RandomizedSet(object):

    def __init__(self):
        self.num_list = []
        self.num_map = {}  # val -> index in self.num_list

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.num_map:
            return False
        
        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.num_map:
            return False
        
        # Index of the element to remove
        idx_to_remove = self.num_map[val]
        last_element = self.num_list[-1]
        
        # Swap the target element with the last element
        self.num_list[idx_to_remove] = last_element
        self.num_map[last_element] = idx_to_remove
        
        # Pop the last element from the list
        self.num_list.pop()
        # Remove the target element from the hash map
        del self.num_map[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.num_list)