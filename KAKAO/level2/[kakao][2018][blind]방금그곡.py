# [kakao][2018][blind]방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

import re
def solution(m, musicinfos):
    answer = ''
    data = []
    titles = []
    musicinfos.sort(key=lambda x:x.split(',')[0])
    j = 1
    for info in musicinfos:
        info = info.split(',')
        start = info[0]
        start = int(start[:2]) * 60 + int(start[3:])
        end = info[1]
        end = int(end[:2]) * 60 + int(end[3:])
        title = info[2]
        melody = re.findall('[A-M]',info[3].replace('A#','H').replace('C#','I').replace('D#','J').replace('E#','K').replace('F#','L').replace('G#','M'))
        temp = ""
        for i in range(start, end):
            temp += melody[(i-start) % len(melody)]
        data.append((title, temp, -j, end - start))

    data.sort(key=lambda x:(x[3], x[2]),reverse=True)
    m = m.replace('A#','H').replace('C#','I').replace('D#','J').replace('E#','K').replace('F#','L').replace('G#','M')
    for i in range(len(data)):
        if m in data[i][1] :
            answer = data[i][0]
            break
    if answer == "":
        answer = "(None)"
    return answer

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  #"HELLO"

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))  #"FOO"
#
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))  #"WORLD"