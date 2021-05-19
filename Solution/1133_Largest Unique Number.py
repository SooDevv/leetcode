from typing import List
from collections import Counter


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counter = Counter(A)
        unique_keys = list(filter(lambda x: counter[x] < 2, counter))
        return max(unique_keys) if unique_keys else -1


if __name__ == '__main__':
    result = Solution().largestUniqueNumber([9, 9, 8, 8 ])
    assert result == -1