"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
整数 N,M に対して、文字列 S_{N,M} を以下のように定義します。
S_{N,M} は o と x からなる長さ M の文字列である。
S_{N,M} の前から k 文字目は、N^k ≤10^9 であれば o 、そうでなければ x である。
整数 N,M が与えられるので、S_{N,M} を出力してください。

制約
N,M は整数である。
1≤N≤10^9
1≤M≤10^5
"""


class Solution:
    @staticmethod
    def ordering(n: int, m: int) -> str:
        o = []
        for k in range(1, m + 1):
            if n ** k <= 10 ** 9:
                o.append("o")
            else:
                x = ["x" for x in range(m - len(o))]
                return ''.join(o+x)
        return ''.join(o)


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(Solution().ordering(N, M))
