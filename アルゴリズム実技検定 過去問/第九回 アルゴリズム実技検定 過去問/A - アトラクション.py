"""
https://atcoder.jp/contests/past202112-open/tasks/past202112_a
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 9 点

問題文
高橋君は遊園地に行きました。
この遊園地のアトラクションに乗るには、以下の条件を全て満たさなければなりません。

身長 H cm 以上
体重 W kg 以下
高橋君は身長 h cm、体重 w kg です。
高橋君はアトラクションに乗ることができますか？

制約
100≤H,h≤200
50≤W,w≤100
入力は全て整数
"""


class Solution:
    @staticmethod
    def attraction(h_rule: int, w_rule: int, h_takahashi: int, w_takahashi: int) -> str:
        return 'Yes' if h_takahashi >= h_rule and w_takahashi <= w_rule else 'No'


if __name__ == '__main__':
    input_H_W, input_h_w = input(), input()
    H, W = map(int, input_H_W.split())
    h, w = map(int, input_h_w.split())
    print(Solution().attraction(H, W, h, w))
