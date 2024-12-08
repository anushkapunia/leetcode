class RandomizedSet(object):

    def __init__(self):
        
        self.val_to_index = {}
        # List to store the values
        self.values = []

        

    def insert(self, val):
        
        if val in self.val_to_index:
            return False
        # Otherwise, add it to the list and dictionary
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True
        """
        :type val: int
        :rtype: bool
        """
        

    def remove(self, val):
        if val not in self.val_to_index:
            return False
        # Get the index of the element to remove
        index = self.val_to_index[val]
        # Get the last element in the list
        last_element = self.values[-1]
        # Swap the element to be removed with the last element
        self.values[index] = last_element
        self.val_to_index[last_element] = index
        # Remove the last element from the list and dictionary
        self.values.pop()
        del self.val_to_index[val]
        return True
        """
        :type val: int
        :rtype: bool
        """
        

    def getRandom(self):
        return random.choice(self.values)
        """
        :rtype: int
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()