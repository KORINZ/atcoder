"""
https://atcoder.jp/contests/abc272/tasks/abc272_a
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 100 点

問題文
N 個の整数 A_1,A_2,…,A_Nが与えられます。
N 個の整数を合計した値を求めてください。

制約
1≤N≤100
1≤A_i≤100
入力はすべて整数
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
