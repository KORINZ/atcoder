"""
https://atcoder.jp/contests/abc266/tasks/abc266_a
"""


class Solution:
    @staticmethod
    def find_middle_letter(s: str) -> str:
        return s[len(s)//2]


if __name__ == '__main__':
    S = input()
    print(Solution.find_middle_letter(S))
