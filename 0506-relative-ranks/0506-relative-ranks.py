class Solution(object):
    def findRelativeRanks(self, score):
        # Create a sorted list of scores with their indices
        sorted_scores = sorted([(v, i) for i, v in enumerate(score)], reverse=True)

        # Create a result list to store the ranks
        result = [""] * len(score)

        # Assign ranks based on the positions in the sorted list
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)

        return result
        