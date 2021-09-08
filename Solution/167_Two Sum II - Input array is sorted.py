from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = []
        for idx, num in enumerate(numbers):
            remains = target - num
            if remains in numbers[idx+1:]:
                return [idx+1, numbers[idx+1:].index(remains)+idx+2]
        return None


if __name__ == '__main__':
    numbers = [0,0,3,4]
    target = 0
    result = Solution().twoSum(numbers, target)
    assert result == [1,2]
