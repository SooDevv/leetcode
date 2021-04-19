class Solution:
    def removeVowels(self, s: str) -> str:
        remove_char_list = 'aeiou'
        result = []
        for char in s:
            if char not in remove_char_list:
                result.append(char)
        return ''.join(result)

    def one_line_code(self, s):
        return "".join(c for c in s if c not in "aeiou")

    def use_regex(self, s):
        import re
        return re.sub('a|e|i|o|u', '', s)


if __name__ == '__main__':
    s = "leetcodeisacommunityforcoders"
    result = Solution().removeVowels(s)
    assert result == "ltcdscmmntyfrcdrs"