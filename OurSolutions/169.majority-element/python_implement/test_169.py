import pytest
import time
import tracemalloc
from solution import Solution

# 多组测试用例
test_cases = [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
    ([1], 1),
    ([4,4,4,4,5,5,5], 4),
    ([6,6,6,7,7], 6),
    ([1,2,3,4,5,5,5,5,5], 5),
]

method_names = [
    "majorityElement_Vote",
    "majorityElement_Dict",
    "majorityElement_Counter",
    "majorityElement_DivMerge",
]

def test_majority_element():
    sol = Solution()
    for nums, expected in test_cases:
        print(f"\nTest nums={nums}, expected={expected}")
        for func_name in method_names:
            func = getattr(sol, func_name)
            tracemalloc.start()
            start_time = time.perf_counter()
            result = func(nums)
            elapsed = time.perf_counter() - start_time
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"  {func_name:25} | result={result} | time={elapsed:.6f}s | peak_mem={peak/1024:.2f}KB")
            assert result == expected
