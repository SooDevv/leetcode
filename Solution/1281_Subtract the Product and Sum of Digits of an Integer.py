class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for i in str(n):
            num = int(i)
            product *= num
            sum += num
        return product-sum



if __name__ == '__main__':
    n = 234
    result = Solution().subtractProductAndSum(n)
    assert result == 15