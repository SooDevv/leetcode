from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # solution #1
        # nums.sort()
        # result = 0
        # for idx, i in enumerate(nums):
        #     if idx % 2 == 0:
        #         result += min(i, i+1)
        # return result

        # solution #2
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    result = Solution().arrayPairSum(nums)
    assert result == 4