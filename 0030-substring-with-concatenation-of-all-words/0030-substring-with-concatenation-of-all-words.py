class Solution(object):
    def findSubstring(self, S, W):
    
        if not W: return []
        LS, M, N, C = len(S), len(W), len(W[0]), collections.Counter(W)
        return [i for i in range(LS-M*N+1) if collections.Counter([S[a:a+N] for a in range(i,i+M*N,N)]) == C]
        