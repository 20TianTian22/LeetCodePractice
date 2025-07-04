from typing import List

class Solution:
    # 最优解法：双指针
    def removeDuplicates_TwoPointers(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # nums[i] 不是重复项
                nums[idx] = nums[i]  # 保留 nums[i]
                idx += 1
        return idx
    
    # 从后往前删除
    def removeDuplicates_Reverse(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
        return len(nums)