import pytest
import time
import tracemalloc
from solution import Solution
    

test_cases = [
    ([1,2,1,2,2,3,3,1], [1,2]),
    ([2,2], [2]),
    ([1,3,3,4], [3]),
    ([4,4,4,4,5,5,5], [4,5]),
    ([1,2,3,4,5,5,5,5,5], [5]),
    ([1,1,1,2,3,4,5,6], [1]),
    ([1,2,3,4,5,6,7,8,9], []),
]

method_names = [
    "majorityElement_Dict",
    "majorityElement_Counter",
    "majorityElement_Vote",
]

@pytest.mark.parametrize("nums, expected", test_cases)
def test_majority_element(nums, expected):
    sol = Solution()
    for func_name in method_names:
        print("")
        func = getattr(sol, func_name)
        tracemalloc.start()
        start_time = time.perf_counter()
        result = func(nums)
        elapsed = time.perf_counter() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{func_name:22} | nums={nums!r:<28} | result={result!r:<10} | expected={expected!r:<10} | time={elapsed:.6f}s | peak_mem={peak/1024:.2f}KB")
        assert sorted(result) == sorted(expected)
