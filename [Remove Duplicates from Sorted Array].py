class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        size = len(nums)
        for j in range(1, size):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1


        
