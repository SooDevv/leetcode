from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_zip = list(zip(*strs))
        prefix = ""
        for i in strs_zip:
            if len(set(i)) == 1: # unique
                prefix += i[0]
            else:
                break
        return prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    result = Solution().longestCommonPrefix(strs)
    assert result == "fl"