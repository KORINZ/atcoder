"""
https://atcoder.jp/contests/abc290/tasks/abc290_a
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 :
100 点

問題文
N 問の問題からなるコンテストが開催され、i (1≤i≤N)問目の配点はA_i点でした。
すぬけくんはこのコンテストに参加し、B_1,B_2,…,B_M問目のM問を解きました。
すぬけくんの総得点を求めてください。
ただし、総得点とは解いた問題の配点の総和を意味するものとします。

制約
1≤M≤N≤100
1≤A_i≤100
1≤B_1<B_2<…<B_M≤N
入力は全て整数
"""
from typing import List


class Solution:
    @staticmethod
    def find_contest_score(points: List[int], correct_questions: List[int]) -> int:
        return sum([points[question - 1] for question in correct_questions])


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(n) for n in input().split()]
    B = [int(n) for n in input().split()]
    print(Solution.find_contest_score(A, B))
