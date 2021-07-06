from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            arr = nums2
        elif len(nums2) == 0:
            arr = nums1
        else:
            arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        if n % 2 == 0:
            i = n // 2
            return (arr[i] + arr[i-1]) / 2
        else:
            return arr[n // 2]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    result = Solution().findMedianSortedArrays(nums1, nums2)
    assert result == 2.0000
