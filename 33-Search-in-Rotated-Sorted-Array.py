class Solution(object):
    def search(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: int
        \\\
        l, r = 0, len(nums)-1

        while r >= l:
            mid = (r + l) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
        