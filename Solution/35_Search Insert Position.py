from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        while s <= e:
            mid = (s+e) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
        return s


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    result = Solution().searchInsert(nums, target)
    assert result == 2