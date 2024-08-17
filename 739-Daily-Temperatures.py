class Solution(object):
    def dailyTemperatures(self, temperatures):
        \\\
        :type temperatures: List[int]
        :rtype: List[int]
        \\\
        result = [0]*len(temperatures)

        stack = []
        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackV, stackI = stack.pop()
                result[stackI] = i - stackI
                
            stack.append((t, i))
        
        return result