class Solution(object):
    def findMin(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        l = 0
        r = len(nums) - 1
        mink = nums[-1]

        while r>l:
            mid = (r+l)//2

            if nums[mid] > mink:
                l = mid + 1

            else:
                mink = nums[mid]
                r = mid
        
        return mink