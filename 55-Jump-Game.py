class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i, v in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+v)
        return True