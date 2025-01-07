class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        length = 0
        set_lst = set(nums)
        for num in set_lst:
            '''
            num
            '''
            if (num - 1) not in set_lst:
                longest = 1

                while (num + longest) in set_lst:
                    longest += 1
            
                length = max(length, longest)
        return length


