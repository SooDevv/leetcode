from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in nums:
            if i != val:
                nums[cnt] = i
                cnt += 1
        return cnt

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    result = Solution().removeElement(nums, val)
    assert result == 2