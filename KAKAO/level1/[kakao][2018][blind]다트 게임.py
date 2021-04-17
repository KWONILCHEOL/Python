# [kakao][2018][blind]다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re
def solution(dartResult):
    dir = {'S':1, 'D':2, 'T':3, '':1, '*':2, '#':-1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*':
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** dir[dart[i][1]] * dir[dart[i][2]]

    return sum(dart)

print(solution("1S2D*3T"))  #37
print(solution("1D2S#10S")) #9
print(solution("1D2S0T"))   #3
print(solution("1S*2T*3S")) #23
print(solution("1D#2S*3S")) #5
print(solution("1T2D3D#"))  #-4
print(solution("1D2S3T*"))  #59