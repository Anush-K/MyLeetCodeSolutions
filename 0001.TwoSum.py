class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1):
                if(i!=j and nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    return result
