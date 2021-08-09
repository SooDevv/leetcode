from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        vol = 0
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        while left < right:
            max_left, max_right = max(height[left], max_left), max(height[right], max_right)

            if max_left <= max_right:
                vol += max_left - height[left]
                left += 1
            else:
                vol += max_right - height[right]
                right -= 1
        return vol


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = Solution().trap(height)
    assert result == 6