"""
https://atcoder.jp/contests/abc272/tasks/abc272_c
"""
from typing import List


class Solution:
    @staticmethod
    def max_even(a: List[int]) -> int:

        odd = [i for i in a if i % 2 != 0]
        even = [i for i in a if i % 2 == 0]

        odd.sort()
        even.sort()

        if len(even) < 2:
            if len(odd) < 2:
                return -1
            else:
                return odd[-1] + odd[-2]
        elif len(odd) < 2:
            return even[-1] + even[-2]
        else:
            return max(odd[-1] + odd[-2], even[-1] + even[-2])


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    print(Solution.max_even(A))
