from typing import List


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        cnt = 0
        max_weight = 5000
        while max_weight > 0 and arr:
            apple = arr.pop(0)
            max_weight -= apple
            if max_weight < 0:
                break
            cnt += 1
        return cnt


if __name__ == '__main__':
    arr = [900, 950, 800, 1000, 700, 800]
    result = Solution().maxNumberOfApples(arr)
    assert result == 5