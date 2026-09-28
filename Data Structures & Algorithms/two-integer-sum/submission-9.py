class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            if target - nums[i] in sol:
                return [min(i,sol[target - nums[i]]),max(i,sol[target-nums[i]])]
            
            sol[nums[i]] = i
