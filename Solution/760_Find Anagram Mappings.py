from typing import List


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = {n: i for i, n in enumerate(B)}
        result = [d[i] for i in A]
        return result


if __name__ == '__main__':
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    result = Solution().anagramMappings(A, B)
    assert result == [1, 4, 3, 2, 0]