class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = False
        seen = []
    

        for x in range(len(nums)):
            if nums[x] in seen:
                r = True
            
            else: 
                seen.append(nums[x])

        return r 