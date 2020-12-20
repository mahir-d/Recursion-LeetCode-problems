class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
​
        max_sum = nums[0]
        curr_sum = nums[0]
        
        for i in range(1, len(nums)):
            
            
            curr_sum = max(nums[i], nums[i] + curr_sum)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        
        return max_sum
            
