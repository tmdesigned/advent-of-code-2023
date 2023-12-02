# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer

number_words = ["zero","one","two","three","four","five","six","seven","eight","nine"]


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    def get_number_from_word(self, text):
        for i,word in enumerate(number_words):
            if(text.lower().find(word) == 0):
                return i
        return None

    @answer(53974)
    def part_1(self) -> int:
        ans = 0
        for line in self.input:
            first = None
            last = None
            for c in line:
                if(c.isdigit()):
                    if(first is None):
                        first = int(c) * 10
                    last = int(c)
            ans += first + last
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        for line in self.input:
            first = None
            last = None
            for i,c in enumerate(line):
                digit = None
                if(c.isdigit()):
                    digit = int(c)
                else:
                    candidate = self.get_number_from_word(line[i:])
                    if(candidate is not None):
                        digit = candidate 
                if digit is not None:
                    if(first is None):
                        first = digit * 10
                    last = digit
            ans += first + last
        return ans


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
