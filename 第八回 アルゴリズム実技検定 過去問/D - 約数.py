"""
https://atcoder.jp/contests/past202109-open/tasks/past202109_d
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
正の整数 X,Y が与えられます。 X の正の約数の個数と Y の正の約数の個数を比較し、
X の正の約数の個数の方が多いなら X と出力し、
Y の正の約数の個数の方が多いなら Y と出力し、
両者が等しいなら Z と出力してください。

制約
1≤X,Y≤10^6
X,Y は整数
"""


class Solution:
    @staticmethod
    def divisor(x: int, y: int) -> str:
        pass


if __name__ == '__main__':
    X, Y = map(int, input().split())
    print(Solution.divisor(X, Y))
