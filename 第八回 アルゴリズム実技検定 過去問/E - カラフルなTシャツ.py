"""
https://atcoder.jp/contests/past202109-open/tasks/past202109_e
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
N 枚の T シャツが売られています。各 T シャツの色は 1 以上 10^9 以下の整数で表され、i 枚目の T シャツの色は c_i で価格は p_i 円です。
K 種類の色の T シャツを集めるには最小で何円必要ですか？
ただし、K 種類の色の T シャツを集めることが不可能な場合は -1 を出力してください。

制約
1≤N≤10^5
1≤K≤N+1
1≤c_i,p_i≤10^9
入力は全て整数である。
"""
from typing import List


class Solution:
    @staticmethod
    def buy_t_shirt(k: int, c: List[int], p: List[int]) -> int:
        bought = dict()

        for c_i, p_i in zip(c, p):

            if c_i not in bought:
                bought[c_i] = p_i

            if p_i < bought[c_i]:
                bought[c_i] = p_i

        if len(bought.keys()) < k:
            return -1
        else:
            return sum(sorted(bought.values())[:k])


if __name__ == '__main__':
    N, K = map(int, input().split())
    C = [int(i) for i in input().split()]
    P = [int(i) for i in input().split()]
    print(Solution.buy_t_shirt(K, C, P))
