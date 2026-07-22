class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, res = 0, float('-inf')
        for i in nums:
            curr = max(i, curr+i)
            res = max(res,curr)
        return res            D