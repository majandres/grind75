# https://leetcode.com/problems/binary-search/

class Solution:
    """Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target < nums[middle]:
                right = middle -1
            elif target > nums[middle]:
                left = middle +1
            else:
                return middle
            
        return -1


s = Solution()
print(s.search([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 15))