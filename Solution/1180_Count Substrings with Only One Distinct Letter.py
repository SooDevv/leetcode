class Solution:
    def countLetters(self, S: str) -> int:
        aaa b a
        a : 3
        aa : 2
        aaa : 1

        b : 1
        a  : 1
        sub_string_list = []
        i = 0
        while i < len(S):
            cur = S[i]
            if cur != tmp:
                i += 1
            i += 1


if __name__ == '__main__':
    S = "aaaba"
    result = Solution().countLetters(S)
    assert result == 8