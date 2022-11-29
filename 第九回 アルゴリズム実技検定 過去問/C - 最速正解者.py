"""
https://atcoder.jp/contests/past202112-open/tasks/past202112_c
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
AtCoder 上で行われたあるコンテストにおいては、問題 A , B , C , D , E , F の 6 問の問題が出題され、全部で N 件の提出がありました。
N 件の提出はすべて異なる時刻に行われ、提出された時間が早いものから順に 1 , 2, … , N と ID がつけられました。
また、全ての提出の結果は AC または WA であり、全ての問題について、その問題に対する提出であって、 結果が AC であるようなものが 1 件以上存在しました。
具体的には、 ID が i である提出は問題 P_i (P_i は A , B , C , D , E , F のいずれか ) に対する提出であり、
その提出結果は V_i (V_i は AC , WA のいずれか ) でした。

問題 A から問題 F までの各問題について、その問題を最初に AC した提出の ID 、
すなわちその問題に対する提出で結果が AC であるようなものであって、 提出 ID が最小であるようなものを求めてください。

制約
6≤N≤1000
P_i は A , B , C , D , E , F のいずれか
V_i は AC , WA のいずれか
各問題について、結果が AC であるような提出が 1 つ以上存在する。
"""
from typing import List


class Solution:
    @staticmethod
    def atcoder(n: int, pv: List[List[str]]) -> dict.values:
        grade_book = {chr(65 + i): 0 for i in range(6)}  # char(65) = "A"

        for i in range(n):
            if pv[i][1] == 'AC' and grade_book[pv[i][0]] == 0:
                grade_book[pv[i][0]] += i + 1
            else:
                pass
        return grade_book.values()


if __name__ == '__main__':
    N = int(input())
    P_V = [list(map(str, input().split())) for i in range(N)]
    for j in Solution().atcoder(N, P_V):
        print(j)
