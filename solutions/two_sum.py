from typing import List


class TwoSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[num] = i
