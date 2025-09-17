'''
iven an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  Brute force method with O(n3)
        n = len(nums)
        lst = []

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        lst.append([nums[i], nums[j], nums[k]])
        
        res = set()
        for x in lst:
            res.add(tuple(sorted(x)))
        
        res1 = [ list(i) for i in res]
        return res1
        
        # Hash based mehtod with O(n)
        n = len(nums)
        res = set()
        if all( x == 0 for x in nums):
            return [[0,0,0]]

        for i in range(n):
            target = -nums[i]
            check = set()

            for j in range(i+1, n):
                complement = target - nums[j]
                if complement in check:
                    res.add(tuple(sorted([nums[i],nums[j],complement])))
                check.add(nums[j])
        
        x = [list(val) for val in res]
        return x
