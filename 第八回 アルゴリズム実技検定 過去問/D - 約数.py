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
from math import sqrt


class Solution:
    @staticmethod
    def count_divisors(n: int) -> int:
        return len({sub for i in range(1, int(sqrt(n)) + 1) for sub in (i, n // i) if n % i == 0})

    @staticmethod
    def compare_divisor(x: int, y: int) -> str:
        if Solution.count_divisors(x) == Solution.count_divisors(y):
            return "Z"
        elif Solution.count_divisors(x) > Solution.count_divisors(y):
            return "X"
        else:
            return "Y"


if __name__ == '__main__':
    X, Y = map(int, input().split())
    print(Solution.compare_divisor(X, Y))
