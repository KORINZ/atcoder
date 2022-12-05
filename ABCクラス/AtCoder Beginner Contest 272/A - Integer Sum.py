"""
https://atcoder.jp/contests/abc272/tasks/abc272_a
"""
from typing import List


class Solution:
    @staticmethod
    def integer_sum(a: List[int]) -> int:
        return sum(a)


if __name__ == '__main__':
    N = input()
    A = [int(i) for i in input().split()]
    print(Solution.integer_sum(A))
