from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums)-1:
            freq = nums[i]
            val = nums[i+1]
            result.extend([val for i in range(freq)])

            i += 2
        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = Solution().decompressRLElist(nums)
    assert result == [2, 4, 4, 4]