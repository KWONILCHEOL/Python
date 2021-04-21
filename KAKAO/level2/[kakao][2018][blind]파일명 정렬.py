# [kakao][2018][blind]파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686

import re
def solution(files):
    answer = []
    FILES = []
    for file in files:
        HEAD = re.split('[0-9]',file)[0]
        NUMBER = re.split('[^0-9]+', file)[1]
        TAIL = file[len(HEAD+NUMBER):]
        FILES.append((HEAD, NUMBER, TAIL))

    FILES.sort(key=lambda x:(x[0].lower(),int(x[1])))
    for HEAD, NUMBER, TAIL in FILES:
        answer.append(HEAD + NUMBER + TAIL)

    return answer

    # a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    # b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    # return b

print(solution(["imga12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))