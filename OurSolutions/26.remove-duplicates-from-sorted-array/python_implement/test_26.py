import pytest
import time
import tracemalloc
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def measure_time_and_memory(func, nums):
    tracemalloc.start()
    start_time = time.perf_counter()

    length = func(nums)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    exec_time = (end_time - start_time) * 1e6  # 转微秒
    peak_kb = peak / 1024  # 转 KB

    return length, exec_time, peak_kb

@pytest.mark.parametrize("nums, expected_nums, expected_len", [
    ([1,1,2], [1,2], 2),
    ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4], 5),
    ([1,2,3], [1,2,3], 3),
    ([1,1,1,1,1], [1], 1),
])
def test_removeDuplicates_TwoPointers(solution, nums, expected_nums, expected_len):
    nums_copy = nums.copy()
    length, exec_time, peak_kb = measure_time_and_memory(solution.removeDuplicates_TwoPointers, nums_copy)

    print(f"\n[TwoPointers] Time: {exec_time:.2f}us, Peak Memory: {peak_kb:.2f} KB")

    assert length == expected_len
    assert nums_copy[:length] == expected_nums

@pytest.mark.parametrize("nums, expected_nums, expected_len", [
    ([1,1,2], [1,2], 2),
    ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4], 5),
    ([1,2,3], [1,2,3], 3),
    ([1,1,1,1,1], [1], 1),
])
def test_removeDuplicates_Reverse(solution, nums, expected_nums, expected_len):
    nums_copy = nums.copy()
    length, exec_time, peak_kb = measure_time_and_memory(solution.removeDuplicates_Reverse, nums_copy)

    print(f"\n[Reverse] Time: {exec_time:.2f}us, Peak Memory: {peak_kb:.2f} KB")

    assert length == expected_len
    assert nums_copy[:length] == expected_nums
