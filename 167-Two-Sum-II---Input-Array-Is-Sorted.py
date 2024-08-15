class Solution(object):
    def twoSum(self, numbers, target):
        \\\
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        \\\
        L=0
        R=len(numbers)-1

        while L<R:
            if numbers[R] + numbers[L]>target:
                R=R-1
            elif numbers[R] + numbers[L]<target:
                L+=1
            else:
                return[L+1, R+1]
        