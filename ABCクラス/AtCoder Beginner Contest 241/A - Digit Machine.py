"""
https://atcoder.jp/contests/abc241/tasks/abc241_a
"""
from typing import List


class Solution:
    @staticmethod
    def use_digital_machine(a: List[int], curr_num: int = 0) -> int:
        return a[a[a[curr_num]]]


if __name__ == '__main__':
    A = [int(i) for i in input().split()]
    print(Solution.use_digital_machine(A))
