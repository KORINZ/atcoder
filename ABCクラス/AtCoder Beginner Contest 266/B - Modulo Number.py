"""
https://atcoder.jp/contests/abc266/tasks/abc266_b
"""


class Solution:
    @staticmethod
    def find_modulo_number(n: int) -> int:
        special_number = 998244353
        return n % special_number


if __name__ == '__main__':
    N = int(input())
    print(Solution.find_modulo_number(N))
