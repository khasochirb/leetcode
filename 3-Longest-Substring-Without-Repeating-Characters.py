class Solution(object):
    def lengthOfLongestSubstring(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        if len(s)==0:
            return 0

        l = 0
        window = set()
        count = []

        for r in range(len(s)):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            count.append(len(window))
            
        return max(count)

            
        