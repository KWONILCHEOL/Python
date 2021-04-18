# [kakao][2021][blind]메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        comb = []
        for order in orders:
            comb += combinations(sorted(order), c)

        counter = Counter(comb)
        if len(counter) == 0:
            continue

        _max = max(counter.values())
        if _max == 1:
            continue

        answer += (''.join(f) for f in counter if counter[f] == _max)
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders,course))  #["AC", "ACDE", "BCFG", "CDE"]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# print(solution(orders,course))  #["ACD", "AD", "ADE", "CD", "XYZ"]
#
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
# print(solution(orders,course))  #["WX", "XY"]