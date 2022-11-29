"""
https://atcoder.jp/contests/past202203-open/tasks/past202203_b
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
高橋君は、A 本の赤い花と B 本の青い花からなる花束をたくさん作りたいです。
赤い花を X 本、青い花を Y 本持っているとき、最大で何個の花束を作れますか？

制約
1≤A,B≤100
0≤X,Y≤100
入力は全て整数
"""


class Solution:
    @staticmethod
    def make_flower(a: int, b: int, x: int, y: int) -> int:
        red, blue = x // a, y // b
        return min(red, blue)


if __name__ == '__main__':
    A, B, X, Y = map(int, input().split())
    print(Solution().make_flower(A, B, X, Y))
