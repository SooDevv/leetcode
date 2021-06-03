from typing import List
from collections import Counter


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        counter = Counter(nums)
        return counter[target] > int(n/2)


if __name__ == '__main__':
    nums = [10,100,101,101]
    target = 101
    result = Solution().isMajorityElement(nums, target)
    assert result == False