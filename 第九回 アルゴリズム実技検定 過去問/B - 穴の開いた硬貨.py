"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
日本で現在使われている硬貨には 1 円玉、5 円玉、10 円玉、50 円玉、100 円玉、500 円玉の 6 種類あります。
これらのうち、穴が開いているものは 5 円玉と 50 円玉の 2 種類です。

高橋君は日本のとある場所で店を経営しており、ある日、彼の店には N 人の客が訪れました。i(1≤i≤N) 番目に訪れた客は A_i 円の品物に対して
B_i 円を支払い、高橋くんはそれぞれの客に対し硬貨の総数が最小になるようにお釣りを出しました。

その日にお釣りとして用いられた硬貨のうち、穴が開いているものは何枚か求めてください。
ただし、高橋くんは 6 種類の硬貨をそれぞれ十分な枚数持っているとします。

制約
1≤N≤10^5
1≤A_i≤B_i≤10^3
入力は全て整数である。
"""
from typing import List


class Solution:
    @staticmethod
    def coins_with_open_hole(price_and_pay: List[List[int]]) -> int:
        change = [pair[1] - pair[0] for pair in price_and_pay]
        coins_with_hole = 0
        for n in change:
            if n % 100 != 0:
                n = n % 100
            if 50 <= n < 100:
                coins_with_hole += 1
            if n % 10 >= 5:
                coins_with_hole += 1
        return coins_with_hole


if __name__ == '__main__':
    N = int(input())
    A_B = [list(map(int, input().split())) for i in range(N)]
    print(Solution().coins_with_open_hole(A_B))
