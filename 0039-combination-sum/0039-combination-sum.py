class Solution(object):
    def combinationSum(self, candidates, target):
   
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
        
        result = []
        candidates.sort()  # Sorting helps to avoid duplicate combinations
        backtrack(0, target, [])
        return result
        