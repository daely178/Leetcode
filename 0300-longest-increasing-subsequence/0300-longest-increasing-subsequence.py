class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
'''
    Constraints O(nlog(n))

    [10,9,2,5,3,7,101,18]

    [2,3,5,7,9,10,18,101]
'''        