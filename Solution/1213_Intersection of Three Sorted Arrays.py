from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = list(set(arr1) & set(arr2) & set(arr3))
        result.sort()
        return result


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    result = Solution().arraysIntersection(arr1, arr2, arr3)
    assert result == [1, 5]