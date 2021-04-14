from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        while n > 0:
            indexs = [nums[0], nums[n]]
            nums.pop(n)
            nums.pop(0)
            result.extend(indexs)
            n -= 1
        return result


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    result = Solution().shuffle(nums, n)
    assert result == [2, 3, 5, 4, 1, 7]