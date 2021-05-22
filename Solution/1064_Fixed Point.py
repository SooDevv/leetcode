from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for idx, val in enumerate(arr):
            if idx == val:
                return idx
        return -1 


if __name__ == '__main__':
    arr = [-10,-5,3,4,7,9]
    result = Solution().fixedPoint(arr)
    assert result == -1