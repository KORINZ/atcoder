"""
https://atcoder.jp/contests/abc241/tasks/abc241_b
"""
from typing import List
from copy import deepcopy


class Solution:
    @staticmethod
    def can_finish_pasta(nums: int, days: int, storage: List[int], plan: List[int]) -> str:

        plan_copy = deepcopy(plan)

        if nums < days:
            return 'No'

        for i in plan_copy:
            if i in storage:
                plan.pop(plan.index(i))
                storage.pop(storage.index(i))
        if not plan:
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(Solution.can_finish_pasta(N, M, A, B))
