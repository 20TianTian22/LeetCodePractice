from typing import List

class Solution:
    def removeDuplicates_DoublePointers(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        ptr = 0
        count = 1 # 默认占一个
        for i in range(1, len(nums)):
            if nums[i] == nums[ptr]:
                if count < 2:
                    ptr += 1
                    nums[ptr] = nums[i]
                    count += 1
            else:
                ptr += 1
                nums[ptr] = nums[i]
                count = 1
        return ptr + 1
    
    def removeDuplicates_Stack(self, nums: List[int]) -> int:
        ptr = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[ptr - 2]:
                nums[ptr] = nums[i]
                ptr += 1
        return min(ptr, len(nums))

        