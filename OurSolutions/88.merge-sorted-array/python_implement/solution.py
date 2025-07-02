from typing import List

class Solution:
    # 方法一：直接合并后排序
    def mergeSorted(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:]=sorted(nums1[:m]+nums2)

    # 方法二：双指针
    def mergeForward(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        idx1, idx2 = 0, 0
        while idx1 < m or idx2 < n:
            if idx1 == m:
                res.append(nums2[idx2])
                idx2 += 1
                """
                下面的这种切片操作会慢点且多耗内存
                res.extend(nums2[idx2:])
                break
                """
            elif idx2 == n:
                res.append(nums1[idx1])
                idx1 += 1
            elif nums1[idx1] < nums2[idx2]:
                res.append(nums1[idx1])
                idx1 += 1
            else:
                res.append(nums2[idx2])
                idx2 += 1
        nums1[:] = res
    # 方法三：逆向双指针
    def mergeBackward(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        idx1, idx2 = 0, 0
        while idx1 < m or idx2 < n:
            if idx1 == m:
                res.append(nums2[idx2])
                idx2 += 1
            elif idx2 == n:
                res.append(nums1[idx1])
                idx1 += 1
            elif nums1[idx1] < nums2[idx2]:
                res.append(nums1[idx1])
                idx1 += 1
            else:
                res.append(nums2[idx2])
                idx2 += 1
        nums1[:] = res





