class Solution(object):
    def carPooling(self, trips, capacity):
      
        changes = [0] * 1001  # Assuming max location is 1000
        
        # Record passenger changes for each trip
        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        
        # Simulate the journey
        current_passengers = 0
        for change in changes:
            current_passengers += change
            if current_passengers > capacity:
                return False
        
        return True
        
        