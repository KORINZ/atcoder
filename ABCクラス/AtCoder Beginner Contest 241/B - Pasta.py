"""
https://atcoder.jp/contests/abc241/tasks/abc241_b
"""
from typing import List


class Solution:
    @staticmethod
    def can_finish_pasta(days: int, storage: List[int], plan: List[int]) -> str:

        for i in range(days):
            if plan[i] in storage:
                storage.remove(plan[i])
            else:
                return 'No'
        return 'Yes'


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(Solution.can_finish_pasta(M, A, B))
