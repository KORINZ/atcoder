"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 9 点

問題文
うさぎとかめが競走をしています。先に X メートル走った方の勝ちです。
うさぎは秒速 A メートル、かめは秒速 B メートルで走ります。
しかし、うさぎはスタートしてから X/2 メートル走った時点で、その場で C 秒間立ち止まって眠ってしまいます。
C 秒間経過すると、うさぎは目を覚まして再び秒速 A メートルで走ります。
レースの勝者を求めてください。ただし、同時にゴールする場合はその旨を出力してください。

制約
1≤X≤10000
1≤A,B≤100
1≤C≤10000
入力は全て整数
"""


class Solution:
    @staticmethod
    def racing(x: int, a: int, b: int, c: int) -> str:
        tortoise_time = x / b
        hare_time = x / a + c

        if tortoise_time == hare_time:
            return 'Tie'
        elif tortoise_time < hare_time:
            return 'Tortoise'
        else:
            return 'Hare'


if __name__ == '__main__':
    X, A, B, C = map(int, input().split())
    print(Solution().racing(X, A, B, C))
