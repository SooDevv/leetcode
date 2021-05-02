import re


class Solution:
    def interpret(self, command: str) -> str:
        command_dict = {'G': 'G', '()': 'o', '(al)': 'al'}
        result = re.sub(r'G|\(()\)|\((al)\)', lambda m: command_dict[m.group()], command)
        return result


if __name__ == '__main__':
    command = "G()(al)"
    result = Solution().interpret(command)
    assert result == "Goal"