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
    exec_time = (end_time - start_time) * 1e6
    peak_kb = peak / 1024
    return length, exec_time, peak_kb

common_test_cases = [
    ([1,1,1,2,2,3], [1,1,2,2,3], 5),
    ([0,0,1,1,1,1,2,3,3], [0,0,1,1,2,3,3], 7),
    ([1,1,1,1], [1,1], 2),
    ([1,2,3], [1,2,3], 3),
    ([], [], 0),
    ([1], [1], 1),
    ([1,1], [1,1], 2),
]

@pytest.mark.parametrize("nums, expected_nums, expected_len", common_test_cases)
def test_removeDuplicates_DoublePointers(solution, nums, expected_nums, expected_len):
    nums_copy = nums.copy()
    length, exec_time, peak_kb = measure_time_and_memory(solution.removeDuplicates_DoublePointers, nums_copy)

    print(f"\n[DoublePointers] Time: {exec_time:.2f}us, Peak Memory: {peak_kb:.2f} KB")

    assert length == expected_len
    assert nums_copy[:length] == expected_nums

@pytest.mark.parametrize("nums, expected_nums, expected_len", common_test_cases)
def test_removeDuplicates_Stack(solution, nums, expected_nums, expected_len):
    nums_copy = nums.copy()
    length, exec_time, peak_kb = measure_time_and_memory(solution.removeDuplicates_Stack, nums_copy)

    print(f"\n[Stack] Time: {exec_time:.2f}us, Peak Memory: {peak_kb:.2f} KB")

    assert length == expected_len
    assert nums_copy[:length] == expected_nums
