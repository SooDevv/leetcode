from typing import List
from collections import defaultdict

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for (n, i) in zip(nums, index):
            target.insert(i, n)
        return target


if __name__ == '__main__':
    nums = [4,2,4,3,2]
    index = [0,0,1,3,1]
    result = Solution().createTargetArray(nums, index)
    assert result == [2,2,4,4,3]