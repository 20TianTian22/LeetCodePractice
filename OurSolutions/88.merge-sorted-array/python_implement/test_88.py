import pytest
import time
import tracemalloc
from solution import Solution

solution = Solution()
list2 = [2, 5, 6]
m = 3
n = 3
expect_res = [1, 2, 2, 3, 5, 6]

@pytest.fixture
def base_list():
    return [1, 2, 3, 0, 0, 0]

def measure_time_and_memory(func, *args):
    tracemalloc.start()
    start_time = time.perf_counter()

    func(*args)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end_time - start_time, peak / 1024  # 返回秒数、KB

def test_sorted_merge(base_list):
    test_list = base_list.copy()
    exec_time, peak_mem = measure_time_and_memory(solution.mergeSorted, test_list, m, list2, n)
    print(f"\nmergeSorted - Time: {exec_time:.6f}s, Peak Memory: {peak_mem:.2f} KB")
    assert test_list == expect_res


def test_mergeForward(base_list):
    test_list = base_list.copy()
    exec_time, peak_mem = measure_time_and_memory(solution.mergeForward, test_list, m, list2, n)
    print(f"\nmergeForward - Time: {exec_time:.6f}s, Peak Memory: {peak_mem:.2f} KB")
    assert test_list == expect_res

def test_mergeBackward(base_list):
    test_list = base_list.copy()
    exec_time, peak_mem = measure_time_and_memory(solution.mergeBackward, test_list, m, list2, n)
    print(f"\nmergeBackward - Time: {exec_time:.6f}s, Peak Memory: {peak_mem:.2f} KB")
    assert test_list == expect_res

