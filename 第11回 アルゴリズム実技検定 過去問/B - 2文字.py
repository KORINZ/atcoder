"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
英小文字のみからなる文字列 S が与えられます。
1≤i≤∣S∣−1 を満たす全ての整数 i について、 S の i 文字目と i+1 文字目をこの順に連結した 2 文字の文字列を書き並べます。
このとき、最も多く書かれる文字列を求めてください。ただし、そのようなものが複数存在する場合、辞書順最小のものを求めてください。

制約
2≤∣S∣≤2×10^5
S は英小文字のみからなる。
"""
from collections import defaultdict


class Solution:
    @staticmethod
    def two_words(s: str) -> str:
        word_dict = defaultdict(int)

        i = 0
        while i < len(s) - 1:
            word_dict[s[i] + s[i + 1]] = word_dict[s[i] + s[i + 1]] + 1
            i += 1

        answer = [k for k, v in word_dict.items() if v == max(word_dict.values())]

        if len(answer) == 1:
            return answer[0]
        else:
            answer.sort()
            return answer[0]


if __name__ == "__main__":
    input_s = str(input())
    print(Solution.two_words(input_s))
