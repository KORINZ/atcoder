"""
https://atcoder.jp/contests/past202203-open/tasks/past202203_c
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
数字と英小文字の変数からなる単項式が 良い単項式 であるとは、英小文字 1 文字の変数の左に 1 以上 999 以下の整数が係数として掛けられているような式を指します。
ただし、係数が 1 であっても、良い単項式ではそれを省略せずに書くものとします。
例えば、 123a や 1z は良い単項式ですが、 0a 、 1000b 、 123 、 12ab 、 a123 、 a などは良い単項式ではありません。

さらに、良い単項式の変数に
a=1000
b=1000a
…
z=1000y
で定まる値を代入したときの値をその良い単項式の値とします。
例えば、 123a の値は 123000 、 20b の値は 20000000 、 1c の値は 1000000000 となります。
良い単項式の値としてあり得るもののうち、 α 以下で最大のものを良い単項式の形で出力してください。
なお、この問題の制約下でそのようなものは必ず一意に存在することが証明できます。

制約
1000≤α<10^81
α は整数
"""


class Solution:
    @staticmethod
    def go_further(a: int) -> str:
        list_a = [c for c in str(a)]
        if len(list_a) % 3 != 0:
            head = len(list_a) % 3
        else:
            head = 3
        res = ''.join([c for c in list_a[0:head]])

        tail = (len(list_a) - head) // 3 - 1
        res += chr(97 + tail)  # chr(97) = "a"
        return res


if __name__ == '__main__':
    alpha = int(input())
    print(Solution().go_further(alpha))
