from typing import List
from collections import Counter

class Solution:
    # 摩尔投票法
    def majorityElement_Vote(self, nums: List[int]) -> int:
        major, vote = 0, 0
        for n in nums:
            if vote == 0:
                major = n
                vote = 1
            elif n == major:
                vote += 1
            else:
                vote -= 1
        return major
    
    # 哈希表计数法
    def majorityElement_Counter(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key=counts.get)
    
    # 使用字典计数法
    def majorityElement_Dict(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        return max(counts, key=counts.get)
        
    # 分治法
    def majorityElement_DivMerge(self, nums: List[int]) -> int:
        def count_in_range(nums: List[int], target: int, low: int, high: int) -> int:
            # 用切片优化
            return nums[low:high+1].count(target)
            # 或者使用循环
            # return sum(1 for i in range(low, high + 1) if nums[i] == target)

        def majority(low: int, high: int) -> int:
            # base case: 只有一个元素
            if low == high:
                return nums[low]

            mid = (low + high) // 2
            left_majority = majority(low, mid)
            right_majority = majority(mid + 1, high)

            if left_majority == right_majority:
                return left_majority

            left_count = count_in_range(nums, left_majority, low, high)
            right_count = count_in_range(nums, right_majority, low, high)

            return left_majority if left_count > right_count else right_majority

        return majority(0, len(nums) - 1)
    
if __name__ == "__main__":
    testList = [1,1,2,2,2,2,3,3,3]
    print(Solution().majorityElement_Vote(testList))
    print(Solution().majorityElement_Dict(testList))
    print(Solution().majorityElement_Counter(testList))
    print(Solution().majorityElement_DivMerge(testList))