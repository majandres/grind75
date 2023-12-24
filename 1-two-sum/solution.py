# https://leetcode.com/problems/two-sum/

class Solution:
    """Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            # print(f'index: {i} ----------------')
            for i2, n2 in enumerate(nums):
                if i2 != i:
                    # print(f'{n}+{n2}={n+n2}')
                    if n + n2 == target:
                        # print(f'Solution found for {nums}, target {target}. Indices: [{i},{i2}]')
                        return [i, i2]

    def twoSumOptimized(self, nums: list[int], target: int) -> list[int]:
        mapa = {}
        for i, n in enumerate(nums):
            desired = target - n
            print(f'checking num {n=}')
            
            # first check if it's in the map
            if desired in mapa:
                if mapa[desired] != i:
                    print(f'Found desired in map: {desired=}')
                    print(f'Solution found for {nums}, target {target} at indices: [{mapa[desired]}, {i}]')
                    return [mapa[desired], i]

            mapa[n] = i

a = Solution()
a.twoSumOptimized([2,7,11,15], 9)
print('===============================')
a.twoSumOptimized([3,2,4], 6)
print('===============================')
a.twoSumOptimized([12,2,9,7,11,15], 18)