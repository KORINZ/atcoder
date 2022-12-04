"""
https://atcoder.jp/contests/abc272/tasks/abc272_b
"""
from typing import List, Set


class Solution:
    @staticmethod
    def is_everyone_friends(n: int, k_x: List[Set[int]]) -> str:

        for person_prev in range(1, n + 1):
            for person_curr in range(person_prev + 1, n + 1):
                for dancing_ordinal in k_x:
                    if person_prev in dancing_ordinal and person_curr in dancing_ordinal:
                        break
                else:
                    return 'No'
        return 'Yes'


if __name__ == '__main__':
    N, M = map(int, input().split())
    K_X = [set([int(i) for i in input().split()][1:]) for i in range(M)]
    print(Solution.is_everyone_friends(N, K_X))
