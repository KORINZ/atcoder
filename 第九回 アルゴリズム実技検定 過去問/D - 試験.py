"""
https://atcoder.jp/contests/past202112-open/tasks/past202112_d
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 :7 点

問題文
AtCoder 高校には N 人の生徒が在籍し、生徒1, 生徒2, …,生徒Nと番号付けられています。
ある日、全員が数学と英語のテストを受け、 生徒i(1≤i≤N)は数学でA_i点、英語でB_i点を取りました。
AtCoder 高校では、次のようにして成績の順位がつけられます。

-数学と英語の合計点が高い生徒が上位
-合計点が等しいとき、数学の点が高い生徒が上位
-合計点および数学の点が等しいとき、番号が小さい生徒が上位

成績が上位の方から順に、N人の生徒番号を出力してください。

制約
2≤N≤2×10^5
0≤A_i≤10^9
0≤B_i≤10^9
入力は全て整数である。
"""
from typing import List


class Solution:
    @staticmethod
    def atcoder_high(n: int, math_grade: List[int], english_grade: List[int]) -> List:
        student_id = [i + 1 for i in range(n)]
        total_grade = [math_grade[i] + english_grade[i] for i in range(n)]
        grade_book = list(zip(total_grade, math_grade, student_id))

        for i in reversed(range(2)):
            grade_book = sorted(grade_book, key=lambda x: x[i], reverse=True)

        return [i[2] for i in grade_book]


if __name__ == '__main__':
    N, A, B = int(input()), list(map(int, input().split())), list(map(int, input().split()))
    print(*Solution().atcoder_high(N, A, B))
