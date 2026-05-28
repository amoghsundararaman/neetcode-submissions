class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, hi = 0, len(nums) - 1

        min_val = nums[hi]

        while low <= hi: 
            mid = low + (hi - low) // 2
            
            if nums[mid] <= nums[hi]:
                min_val = min(min_val, nums[mid])
                hi = mid - 1
            else:
                min_val = min(min_val, nums[mid])
                low = mid + 1
        return min_val

                
        