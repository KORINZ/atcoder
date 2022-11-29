"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 8 点

問題文
それぞれ N 個、M 個の正整数からなる 2 つの数列 A=(A_1,A_2,…,A_N) と B=(B_1,B_2,…,B _M) が与えられます。
A と B の両方に含まれる要素を全て求め、値の小さい順に出力してください。

制約
1≤N,M≤1000
1≤A_i≤10^9
1≤B_i≤10^9
i≠j ならば A_i≠A_j
i≠j ならば B_i≠B_j
入力は全て整数
"""
from typing import Set, List, Union


class Solution:
    @staticmethod
    def product_set(n: int, m: int, a_n: Set[int], b_m: Set[int]) -> List[Union[int, None]]:

        if a_n == b_m:
            return sorted(a_n)

        if n > m:
            ans = [i for i in b_m if i in a_n]
        else:
            ans = [i for i in a_n if i in b_m]
        return sorted(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = {int(i) for i in input().split()}
    B = {int(i) for i in input().split()}
    print(*Solution.product_set(N, M, A, B))
