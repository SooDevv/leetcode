from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair_dict = Counter(nums)
        result = 0
        for i in pair_dict.values():
            if i > 1:
                sum = factorial(i-1)
                result += sum
        return result


def in_cache(func):
    cache = {}
    def _wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return _wrapper


@in_cache
def factorial(n):
    return n + factorial(n-1) if n > 1 else 1


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    result = Solution().numIdenticalPairs(nums)
    print(result)
