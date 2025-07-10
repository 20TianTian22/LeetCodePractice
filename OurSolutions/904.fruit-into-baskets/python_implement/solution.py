from typing import List
import collections

class Solution:
    def totalFruit_Deque(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1

        queue = collections.deque()
        l = 0
        temp = 0
        res = 1

        for r in range(len(fruits)):
            if fruits[r] not in queue:
                if len(queue) == 2:
                    queue.popleft()
                    l = temp
                temp = r
                queue.append(fruits[r])
            else:
                if fruits[r] != queue[-1]:
                    queue.popleft()
                    temp = r
                    queue.append(fruits[r])
            res = max(res, r - l + 1)

        return res
    
    def totalFruit_Dict(self, fruits: List[int]) -> int:
        fruit_dict = {}  # key: 水果种类, value: 该水果最后一次出现的索引
        l = 0
        res = 0

        for r, fruit in enumerate(fruits):
            fruit_dict[fruit] = r

            if len(fruit_dict) > 2:
                # 找出最左边水果的最后索引
                min_idx = min(fruit_dict.values())
                # 更新左边界
                l = min_idx + 1
                # 从字典里删掉它
                del_fruit = [key for key, val in fruit_dict.items() if val == min_idx][0]
                del fruit_dict[del_fruit]

            res = max(res, r - l + 1)

        return res

        

        





