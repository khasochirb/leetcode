class Solution(object):
    def isPalindrome(self, x):
        \\\
        :type x: int
        :rtype: bool
        \\\
        string = str(x)
        half = len(string)//2

        for i in range(0, half):
            if string[i]!=string[-(i+1)]:
                return False
        return True

        