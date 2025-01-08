class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        result = 0
        R = 1
        L = 0

        while R<len(prices):
            
            if prices[R] > prices[L]:
                
                diff = prices[R] - prices[L]
                result = max(result, diff)
                R +=1
            else:
                L = R
                R = R+1


        return result
