"""
実行時間制限: 2 sec / メモリ制限: 1024 MB
配点 : 7 点

問題文
YYYY/MM/DD 形式とは日付の表記方法の 1 つで、0 埋めした 4 桁の西暦年、0 埋めした 2 桁の月、 0 埋めした 2 桁の日をスラッシュで区切って並べたものを言います。
たとえば 2022 年 1 月 1 日は 2022/01/01 と表されます。
日付を YYYY/MM/DD 形式で表したときに表れる数字が 2 種類以下であるとき、良い 日付と呼びます。
日付 S が YYYY/MM/DD 形式で与えられます。S 以降の日で はじめて 現れる良い日付を YYYY/MM/DD 形式で出力してください。
ただし、暦はグレゴリオ暦 (現行の日本をはじめ世界各国で使用されている暦) を使用するものとします。

制約
S はグレゴリオ暦に現れる日付である。
S は YYYY/MM/DD 形式で与えられる。
S は 2001 年 1 月 1 日以降 2999 年 12 月 31 日以前である。
"""


class Solution:
    @staticmethod
    def good_date(s: str) -> str:
        s = int(''.join(s.split("/")))
        starting_year = s // 10000

        for yyyy in range(starting_year, 3001):
            for mm in range(2, 13):
                for dd in range(1, 23):

                    date = str(yyyy) + f"{mm:02}" + f"{dd:02}"

                    if len(set(date)) != 2:  # skip if the length of set(date) is not uniquely 2
                        continue

                    if str(s) <= date:
                        return date[:4] + "/" + date[4:6] + "/" + date[6:]


if __name__ == '__main__':
    S = str(input())
    print(Solution().good_date(S))
