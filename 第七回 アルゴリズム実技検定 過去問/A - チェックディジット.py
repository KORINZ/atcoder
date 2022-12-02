"""
https://atcoder.jp/contests/past202107-open/tasks/past202107_a
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 9 点

問題文
高橋君は、15 桁の数字で作られたコード S を発行しました。 S は 0, … , 9 のみからなる、長さ 15 の文字列です。
この 15 桁のコードの、一番右の桁は、チェックディジットとなっており、残りの 14 桁から計算することが可能です。
まず、左の 14 桁のうち、左から奇数番目の数 (一番左の数を 1 番目と数えます) をすべて足し、その値を 3 倍します。
次に、こうして得られた値に、左から偶数番目の数をすべて足します。その値を 10 で割った余りが 15 桁目の数と一致するのが正しいコードで、
一致しないのは正しくないコードです。
高橋君の代わりに、コード S が正しいかどうか判定するプログラムを作成してください。

制約
S の長さは 15
S は 0, … , 9 のみからなる
"""


class Solution:
    @staticmethod
    def check_digit(s: str) -> str:
        odd_sum = sum([int(i) for i in s[:14][::2]]) * 3
        even_sum = sum([int(i) for i in s[1:][::2]])

        if (odd_sum + even_sum) % 10 == int(s[-1]):
            return 'Yes'
        else:
            return 'No'


if __name__ == '__main__':
    S = str(input())
    print(Solution.check_digit(S))
