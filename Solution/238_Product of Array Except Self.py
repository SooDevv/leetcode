from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        answer[0] = 1

        for i in range(1, len(nums)):
            answer[i] = nums[i-1] * answer[i-1]

        R = 1
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = Solution().productExceptSelf(nums)
    assert result == [24, 12, 8, 6]