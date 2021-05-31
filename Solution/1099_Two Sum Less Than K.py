from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        num_less_k = list(filter(lambda x: x < k, nums))
        if len(num_less_k) <= 1: return -1

        num_less_k.sort()
        max_val = 0
        while num_less_k:
            max_cur = num_less_k.pop()
            for i in num_less_k:
                val = max_cur + i
                if max_val < val < k:
                    max_val = val
                else:
                    continue
        return max_val


if __name__ == '__main__':
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    k = 60
    result = Solution().twoSumLessThanK(nums, k)
    assert result == 58