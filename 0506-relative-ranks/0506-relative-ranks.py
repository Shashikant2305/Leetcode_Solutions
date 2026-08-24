class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        
        # score ke saath original index
        arr = [(score[i], i) for i in range(n)]
        
        # highest score first
        arr.sort(reverse=True)
        
        ans = [""] * n
        
        for rank, (s, idx) in enumerate(arr):
            if rank == 0:
                ans[idx] = "Gold Medal"
            elif rank == 1:
                ans[idx] = "Silver Medal"
            elif rank == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank + 1)
        
        return ans