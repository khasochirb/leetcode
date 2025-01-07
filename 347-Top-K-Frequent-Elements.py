class Solution(object):
    def topKFrequent(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \\\
        count = { }
        nums_lst = []
        result = []



        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)


        for num, c in count.items():
            nums_lst.append([c,num])
            
        nums_lst.sort()

        for i in range(len(nums_lst)-1, len(nums_lst)-k-1, -1):
            result.append(nums_lst[i][1])


        return result

        