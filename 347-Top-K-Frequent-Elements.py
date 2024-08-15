class Solution(object):
    def topKFrequent(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        \\\
        ans = defaultdict(int)

        
        for i in range(len(nums)):
            ans[nums[i]] += 1
        top_k = sorted(ans.items(), key = lambda x:x[1], reverse = True)[:k]
        top_k_keys = [key for key, value in top_k]

        return top_k_keys