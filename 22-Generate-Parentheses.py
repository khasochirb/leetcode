class Solution(object):
    def generateParenthesis(self, n):
        \\\
        :type n: int
        :rtype: List[str]
        \\\
        
        result = []
        stack = []

        def bt(left, right):

            if left == right == n:
                result.append(\\.join(stack))
                return

            if left < n:
                stack.append(\(\)
                bt(left+1, right)
                stack.pop()
            
            if right < left:
                stack.append(\)\)
                bt(left, right+1)
                stack.pop()
        
        bt(0, 0)
        return result