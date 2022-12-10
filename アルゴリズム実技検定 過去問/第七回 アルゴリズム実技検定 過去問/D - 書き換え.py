"""
https://atcoder.jp/contests/past202107-open/tasks/past202107_d
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
長さ N の文字列 S があります。
あなたは、以下の操作を好きな回数だけ行うことができます。

S の(連続する)部分文字列で、axa , ixi , uxu , exe , oxo のいずれかと一致する部分を ... に書き換える。

あなたは、操作を可能な限り多く行いたいと思っています。
操作回数が最大となるように操作を行った後の S を 1 つ出力してください。

制約
1≤N≤2×10^5
S は 英小文字からなる長さ N の文字列。
"""


class Solution:
    @staticmethod
    def replace_strings(s: str) -> str:
        result = ""
        match_sets = {"axa", "ixi", "uxu", "exe", "oxo"}

        i = 0
        while i < len(s):
            if s[i:i + 3] in match_sets:
                result += "..."
                i += 3
            else:
                result += s[i]
                i += 1

        return result


if __name__ == '__main__':
    N = int(input())
    S = input()
    print(Solution.replace_strings(S))
