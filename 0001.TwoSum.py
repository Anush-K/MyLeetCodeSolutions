"""
Question
--------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

"""
Answer
------
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1):
                if(i!=j and nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    return result
