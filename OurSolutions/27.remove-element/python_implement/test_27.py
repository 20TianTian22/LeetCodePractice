import pytest
import time
import tracemalloc
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def measure_time_and_memory(func, nums, val):
    tracemalloc.start()
    start_time = time.perf_counter()

    length = func(nums, val)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    exec_time = (end_time - start_time) * 1e6  # 微秒
    peak_kb = peak / 1024  # 转成 KB

    return length, exec_time, peak_kb

@pytest.mark.parametrize("nums, val, expected_nums, expected_len", [
    ([3,2,2,3], 3, [2,2], 2),
    ([0,1,2,2,3,0,4,2], 2, [0,1,3,0,4], 5),
    ([1,1,1,1], 1, [], 0),
    ([4,5], 3, [4,5], 2),
    ([], 0, [], 0)
])
def test_removeElement_Remove(solution, nums, val, expected_nums, expected_len):
    nums_copy = nums.copy()
    length, exec_time, peak_kb = measure_time_and_memory(solution.removeElement_Remove, nums_copy, val)

    print(f"\n[Remove] Time: {exec_time:.2f}us, Peak Memory: {peak_kb:.2f} KB")

    assert length == expected_len
    assert sorted(nums_copy[:length]) == sorted(expected_nums)

@pytest.mark.parametrize("nums, val, expected_nums, expected_len", [
    ([3,2,2,3], 3, [2,2], 2),
    ([0,1,2,2,3,0,4,2], 2, [0,1,3,0,4], 5),
    ([1,1,1,1], 1, [], 0),
    ([4,5], 3, [4,5], 2),
    ([], 0, [], 0)
])
def test_removeElement_Stack(solution, nums, val, expected_nums, expected_len):
    nums_copy = nums.copy()
    length, exec_time, peak_kb = measure_time_and_memory(solution.removeElement_Stack, nums_copy, val)

    print(f"\n[Stack] Time: {exec_time:.2f}us, Peak Memory: {peak_kb:.2f} KB")

    assert length == expected_len
    assert sorted(nums_copy[:length]) == sorted(expected_nums)
