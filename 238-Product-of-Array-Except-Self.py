class Solution(object):
    def productExceptSelf(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[int]
        \\\
        lst = [1]*len(nums)
        
        for i in range(1, len(nums)):
            lst[i] *= lst[i-1]*nums[i-1]
        reverse = 1
        for i in range(len(nums)-1, -1, -1):
            lst[i] *= reverse
            reverse *= nums[i]
        
        return lst