"""
https://atcoder.jp/contests/past202203-open/tasks/past202203_d
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
高橋君はある同じ試験を T 回受験しました。各試験は 1 から N の番号のついた N 科目からなります。
高橋君は i 回目の試験では科目 j で P_{i,j} 点をとりました。
K=1,2,…,T について次の問題に答えてください。

問題：
K 回目まで( K 回目含む)の試験の結果のうち、科目 j の最高得点を C_j とする。C_1+…+C_N を求めよ。

制約
1≤T≤10^3
1≤N≤10
0≤P_{i,j}≤10^5
入力に含まれる値は全て整数である
"""
from typing import List


class Solution:
    @staticmethod
    def high_score(p: List[List[int]]) -> List[int]:
        current_high_score = p[0]
        score_list = [sum(current_high_score)]

        for i in p[1:]:
            for j in range(len(i)):
                if i[j] > current_high_score[j]:
                    current_high_score[j] = i[j]
            score_list.append(sum(current_high_score))

        return score_list


if __name__ == '__main__':
    T_N = list(map(int, input().split()))
    P = [list(map(int, input().split())) for i in range(T_N[0])]
    for i in Solution().high_score(P):
        print(i)
