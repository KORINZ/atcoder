"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
英小文字の組 (a_1,b_1), (a_2,b_2),…,(a_N,b_N) があります。
英小文字 u,v が 似ている とは、(u,v)=(a_i, b_i) または (u,v)=(b_i,a_i) を満たす i が存在することを言います。
また、長さの等しい英小文字からなる文字列 U,V が 似ている とは、U,V が次の条件を満たすことを言います。
U の文字を 1 つ選んで、似ている文字に置き換えることを好きなだけ繰り返したとき(操作をしなくてもよい)、V に一致させることができる。
長さの等しい文字列 S,T が与えらえるので、S と T が似ているか判定してください。

制約
1≤N≤325
N は整数である。
a_i ,b_i は互いに異なる英小文字である。
i != j ならば (a_i,b_i) != (a_j,b_j) かつ (a_i,b_i) != (b_j,a_j) が成り立つ。
S,T は英小文字からなる長さ 1 以上 100 以下の文字列である。
S の長さと T の長さは等しい。
"""
from typing import List


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def similar_words(n: int, ab: List, s: str, t: str) -> bool:
        pass


if __name__ == '__main__':
    pass
    # print(Solution().similar_words())
