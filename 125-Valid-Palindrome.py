class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        letters = re.sub('[\\W_]+', '', s)
        reverse = letters[::-1]
        
        return reverse.lower()==letters.lower()
        