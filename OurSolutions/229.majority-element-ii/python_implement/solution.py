from typing import List
from collections import Counter
class Solution:
    def majorityElement_Dict(self, nums: List[int]) -> List[int]:
        cnt = {}
        ans = []

        for v in nums:
            if v in cnt:
                cnt[v] += 1
            else:
                cnt[v] = 1
        for item in cnt.keys():
            if cnt[item] > len(nums)//3:
                ans.append(item)
        return ans
    
    def majorityElement_Counter(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        return [num for num, cnt in counts.items() if cnt > len(nums)//3]

    def majorityElement_Vote(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        # 只遍历一次统计两个候选人的出现次数
        cnt1 = cnt2 = 0
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
        result = []
        if cnt1 > len(nums) // 3:
            result.append(candidate1)
        if cnt2 > len(nums) // 3:
            result.append(candidate2)
        return result
    





