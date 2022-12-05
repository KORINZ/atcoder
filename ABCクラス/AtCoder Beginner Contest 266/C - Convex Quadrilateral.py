"""
https://atcoder.jp/contests/abc266/tasks/abc266_c
"""
from typing import List, Tuple


class Solution:
    @staticmethod
    def is_valid(x, y, z):
        x1 = y[0] - x[0]
        y1 = y[1] - x[1]
        x2 = z[0] - x[0]
        y2 = z[1] - x[1]

        if x1 * y2 - x2 * y1 > 0:
            return True
        else:
            return False

    @staticmethod
    def check_convex_quadrilateral(a_b_c_d: List[Tuple[int]]) -> str:
        a, b, c, d = a_b_c_d

        if Solution.is_valid(a, b, d) \
                and Solution.is_valid(b, c, a) \
                and Solution.is_valid(c, d, b) \
                and Solution.is_valid(d, a, c):
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    A_B_C_D = [tuple(int(i) for i in input().split()) for i in range(4)]
    print(Solution.check_convex_quadrilateral(A_B_C_D))
