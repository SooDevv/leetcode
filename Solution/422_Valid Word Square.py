from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        i = 0
        while i < n:
            word = words[i]
            point_list = []
            for w in words:
                try:
                    a = w[i]
                except:
                    a = ''
                point_list.append(a)
            tmp = ''.join(point_list)
            if word == tmp:
                i += 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    words = ["abcd","bnrt","crm","dt"]
    result = Solution().validWordSquare(words)
    assert result == True