import pytest
import time
import tracemalloc
from solution import Solution

test_cases = [
    ([1], 1),
    ([1,2], 2),
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4),
    ([3,3,3,1,2,1,1,2,3,3,4], 5),
    ([1,2,1,2,1,2,1,2], 8),
    ([1,2,3,4,5], 2),
    ([1,1,1,1,1], 5),
]

method_names = [
    "totalFruit_Deque",
    "totalFruit_Dict",
]

@pytest.mark.parametrize("fruits, expected", test_cases)
def test_total_fruit(fruits, expected):
    sol = Solution()
    for func_name in method_names:
        func = getattr(sol, func_name)
        tracemalloc.start()
        start_time = time.perf_counter()
        result = func(fruits)
        elapsed = time.perf_counter() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"\n{func_name:18} | fruits={fruits!r:<40} | result={result:<3} | expected={expected:<3} | time={elapsed:.6f}s | peak_mem={peak/1024:.2f}KB")
        assert result == expected
