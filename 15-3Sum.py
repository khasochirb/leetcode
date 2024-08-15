class Solution(object):
    def threeSum(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[List[int]]
        \\\
        lst = []
    
        nums.sort()
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                    
            if nums[i] <= 0:
                l1 = i
                l2 = i + 1
                r = len(nums) - 1
                
                while l2 < r:
                    summ = nums[l1] + nums[l2] + nums[r]
                    
                    if summ > 0:
                        r -= 1
                    elif summ < 0:
                        l2 += 1
                    
                    else:
                        lst.append([nums[l1], nums[l2], nums[r]])
                        l2 += 1
                        r -= 1
                        while nums[l2] == nums[l2 - 1] and l2 < r:
                            l2 += 1
            else:
                break
                
            
        
        return lst