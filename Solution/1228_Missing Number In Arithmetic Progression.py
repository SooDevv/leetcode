from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        s, e = arr[0], arr[-1]

        total = abs(s - e)
        gap = int(total / len(arr))

        if s < e:
            origin_set = set(range(s, e+1, gap))
        elif s > e:
            origin_set = set(range(e, s + 1, gap))
        elif s == e:
            return s
        return list(origin_set - set(arr))[0]


if __name__ == '__main__':
    arr = [0,0,0,0,0]
    result = Solution().missingNumber(arr)
    assert result == 14