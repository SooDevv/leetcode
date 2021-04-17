from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        negative_values = list(filter(lambda x: x < 0, nums))
        return 1 if len(negative_values) % 2 == 0 else -1


if __name__ == '__main__':
    nums = [-1,-2,-3,-4,3,2,1]
    result = Solution().arraySign(nums)
    assert result == 1