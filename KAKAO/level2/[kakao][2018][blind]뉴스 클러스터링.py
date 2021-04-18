# [kakao][2018][blind]뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

import re
def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if len(re.findall('[a-zA-Z]', str1[i:i+2])) == 2]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if len(re.findall('[a-zA-Z]', str2[i:i+2])) == 2]

    cnt = 0
    total = 0
    for s in str1:
        total += 1
        if s in str2:
            str2.remove(s)
            cnt += 1
    total += len(str2)
    if cnt == total: answer = 65536
    else: answer = int(cnt / total * 65536)
    return answer

str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2)) #16384

str1 = "handshake"
str2 = "shake hands"
print(solution(str1, str2)) #65536

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2)) #43690

str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(solution(str1, str2)) #65536