class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        cursum = 0

        for n in nums:
            cursum = max(cursum, 0)
            cursum += n
            maxsum = max(maxsum, cursum)

        return maxsum