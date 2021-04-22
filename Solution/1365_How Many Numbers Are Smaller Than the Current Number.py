from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = {}
        for i, n in enumerate(sorted(nums)):
            if n not in result:
                result[n] = i
        return [result[n] for n in nums]


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    result = Solution().smallerNumbersThanCurrent(nums)
    print(result)