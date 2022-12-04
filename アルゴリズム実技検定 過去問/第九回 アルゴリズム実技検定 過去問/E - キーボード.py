"""
https://atcoder.jp/contests/past202112-open/tasks/past202112_e
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
高橋君は整数 N をキーボードを使って入力しようと考えています。
高橋君は各桁の数字のうち、1 , 2 , 3 , 4 , 5 は左手を用いて、6 , 7 , 8 , 9 , 0 は右手を用いて入力します。
高橋君が各桁の数字を打ち込むのにかかる時間は以下の通りです。

打ち込みたい数字が整数の先頭の桁であるとき、数字によらず 500ms かかる。
そうでなく、打ち込みたい数字が直前の数字と同じであるとき、301ms かかる。
上の 2 つに該当せず、打ち込みたい数字が直前の数字を打ち込むのに用いた手と同一の手を用いるとき、210ms かかる。
それ以外のとき、100ms かかる。
整数を入力するのにかかる時間は各桁を打ち込むのにかかる時間の総和です。高橋君が整数 N を入力するのにかかる時間が何 ms であるか求めてください。

制約
1≤N<10^200000
N の先頭の桁は 0 ではない。
N は整数
"""
from copy import deepcopy


class Solution:
    @staticmethod
    def key_board(n: str) -> int:

        left_num, right_num = set(), set()
        for i in range(10):
            if 1 <= i <= 5:
                left_num.add(str(i))
            else:
                right_num.add(str(i))

        res = 500
        s = deepcopy(n)

        for i, n in enumerate(n[1:], start=1):
            if n == s[i - 1]:
                res += 301
            elif n in left_num and s[i - 1] in left_num or n in right_num and s[i - 1] in right_num:
                res += 210
            else:
                res += 100
        return res


if __name__ == '__main__':
    N = str(input())
    print(Solution().key_board(N))
