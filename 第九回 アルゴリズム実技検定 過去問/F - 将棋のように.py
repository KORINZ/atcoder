"""
https://atcoder.jp/contests/past202112-open/tasks/past202112_f
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
縦 9 行、横 9 列からなるマス目があり、上から i 行目、左から j 列目のマスを (i,j) と表すことにします。
はじめ、マス (A,B) にコマが一つ置かれています。その他のマスにはコマは置かれていません。

コマは、自身が存在するマスの 8 近傍に位置するマスのうちいくつかに一手で移動することができます。
移動することのできるマスの集合の具体的な情報は長さがそれぞれ 3 である 3 つの文字列 S_1 ,S_2 ,S_3 によって表され、
コマがあるマス (x,y) に存在するとき、

S_i の j 文字目が # ならマス (x+i−2,y+j−2) に一手で移動することが可能
S_i の j 文字目が . ならマス (x+i−2,y+j−2) に一手で移動することは不可能

です。ただし、マス目の外に出るような移動をすることはできません。
0 回以上の移動によってコマが辿り着けるマスの個数を求めてください。

制約
1≤A,B≤9
S_1 ,S_2 ,S_3 はそれぞれ # と . のみからなる長さ 3 の文字列
S_2 の 2 文字目は .
A,B は整数
"""
from typing import List


class Solution:
    @staticmethod
    def shogi(a_b: List[int], s_1: str, s_2: str, s_3: str) -> int:
        pass


if __name__ == '__main__':
    A_B = list(map(int, input().split('')))
    S_1, S_2, S_3 = str(input()), str(input()), str(input())
    print(Solution().shogi(A_B, S_1, S_2, S_3))
