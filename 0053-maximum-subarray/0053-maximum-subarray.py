class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=nums[0]
        total=0
        for n in nums:
            if total<0:
                total=0
            total+=n
            result=max(result,total)
        return result
