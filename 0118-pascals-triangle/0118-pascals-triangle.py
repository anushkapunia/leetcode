class Solution(object):
    def generateRow(self, row):
        
        ans = 1
        
        # Inserting the 1st element
        ansRow = [1] 

        # Calculate the rest of the elements
        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansRow.append(ans)

        return ansRow

    """ Function to generate Pascal's
    Triangle up to n rows"""
    def generate(self, n):
        pascalTriangle = []
        for row in range(1, n + 1):
            pascalTriangle.append(self.generateRow(row))

        # Return the Pascal's Triangle
        return pascalTriangle
