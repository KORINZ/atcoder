"""
https://atcoder.jp/contests/past202109-open/tasks/past202109_c
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
長さ N の整数列 A=(A_1,A_2,…,A_N) が与えられます。この整数列の中に整数 X は何回現れますか？

制約
1≤N≤10^5
1≤X≤10^9
1≤A_i≤10^9
入力は全て整数である。
"""
from typing import List


class Solution:
    @staticmethod
    def appearance(x: int, a: List[int]) -> int:
        return a.count(x)


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = [int(i) for i in input().split()]
    print(Solution.appearance(X, A))
