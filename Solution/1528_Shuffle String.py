from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str_2_idx_tuple = [(char, idx) for char, idx in zip(s, indices)]
        str_2_idx_tuple.sort(key=lambda x: x[1])
        result = [i[0] for i in str_2_idx_tuple]
        return ''.join(result)

    def otherSolution(self,  s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for idx, elm in enumerate(zip(indices, s)):
            result[elm[0]] = elm[1]
        return ''.join(result)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    result = Solution().restoreString(s, indices)
    assert result == 'leetcode'