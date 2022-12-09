"""
https://atcoder.jp/contests/past202107-open/tasks/past202107_c
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
0 から 9 の数字からなる文字列 S が与えられます。
S を整数の十進数表示として見たとき、以下の 2 つの条件をともに満たすかどうか判定してください。

先頭に不要な 0 がない。
L 以上 R 以下である。

制約
S は 0 から 9 の数字からなる文字列
1≤∣S∣≤100
0≤L≤R≤10^9
L と R は整数
"""


class Solution:
    @staticmethod
    def check_input(s: str, left: int, right: int) -> str:
        if s[0] == "0" and len(s) != 1:
            return 'No'

        if left <= int(s) <= right:
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    S = input()
    L, R = map(int, input().split())
    print(Solution.check_input(S, L, R))
