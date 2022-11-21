"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 9 点

問題文
3 枚のカードがあります。 1 枚目のカードには整数 A が、2 枚目のカードには整数 B が、3 枚目のカードには整数 C が書かれています。
3 枚のカードの中から 2 枚のカードを選ぶとき、選んだ 2 枚に書かれた整数の積としてあり得る最小値と最大値を出力して下さい。

制約
−100≤A,B,C≤100
A,B,C は整数
"""


class Solution:
    @staticmethod
    def three_cards(a: int, b: int, c: int):
        product_res = [a * b, a * c, b * c]
        return ' '.join(map(str, [min(product_res), max(product_res)]))


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(Solution().three_cards(A, B, C))
