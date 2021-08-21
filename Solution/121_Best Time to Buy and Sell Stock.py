from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        min_price = sys.maxsize

        for p in prices:
            min_price = min(min_price, p)
            output = max(output, p - min_price)
        return output


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    assert result == 5