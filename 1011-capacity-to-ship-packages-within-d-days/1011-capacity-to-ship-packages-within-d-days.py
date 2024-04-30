class Solution(object):
    def shipWithinDays(self, weights, days):
        l , r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            n = 1
            c = 0
            for w in weights:
                if c + w > mid:
                    n += 1
                    c = 0
                c += w
            if n > days:
                l = mid + 1
            else:
                r = mid
        return l
