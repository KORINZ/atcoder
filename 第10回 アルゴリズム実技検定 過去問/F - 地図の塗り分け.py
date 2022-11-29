"""
https://atcoder.jp/contests/past202203-open/tasks/past202203_f
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
高橋王国は 1 から N までの番号がついた N 個の州からなります。
高橋王国の地図は H 行 W 列のマス目の形をしていて、上から i 行目、左から j 列目のマスは州 A_{i,j} です。
この地図の州 i を色 C_i で塗るとき、以下の条件は満たされていますか？

異なる州が上下左右に隣り合っているならば、それらの州は異なる色で塗られている

制約
1≤H≤200
1≤W≤200
1≤N≤min(100,H×W)
1≤A_{i,j}≤N
全ての k(1≤k≤N) について、A_{i,j}=k を満たす (i,j) が少なくとも 1 つ存在する
1≤C_i≤N
入力に含まれる値は全て整数である
"""


class Solution:
    @staticmethod
    def color_map():
        pass


if __name__ == '__main__':
    pass
