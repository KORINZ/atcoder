"""
https://atcoder.jp/contests/past202109-open/tasks/past202109_a
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 9 点

問題文
レストランに来た高橋君は A 円のランチと B 円のドリンクバーを注文しようとしています。
高橋君は C 円引きのドリンクバー割引券を持っており、割引券を利用すると合計 A+B－C 円で注文することができます。
一方、ランチとドリンクバーのセットメニューを D 円で注文することもできますが、割引券を適用することはできません。
高橋君がランチとドリンクバーの両方を注文するのに必要な最小の金額を出力してください。

制約
1≤A≤1000
1≤C<B≤1000
1≤D≤1000
入力は全て整数である。
"""
from typing import List


class Solution:
    @staticmethod
    def drink_bar(a_b_c_d: List[int]) -> int:
        a, b, c, d = a_b_c_d
        with_coupon, without_coupon = a + b - c, d
        return min(with_coupon, without_coupon)


if __name__ == '__main__':
    A_B_C_D = [int(i) for i in input().split()]
    print(Solution.drink_bar(A_B_C_D))
