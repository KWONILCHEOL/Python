# [kakao][2019][intern]튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

import re
from collections import Counter
def solution(s):
    answer = []
    s = Counter(re.findall('\d+', s))
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    return list(map(int, [x[0] for x in s]))
    

def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    new_s = []
    
    for i in s:
        new_s.append(i.split(','))
    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer