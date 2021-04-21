# [kakao][2018][blind]추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676

# 끝점을 기준으로 정렬
# 끝점 + 1 초 보다 시작점이 작으면 카운트(+1)

def solution(lines):
    answer = 1
    for i in range(len(lines)):
        line = lines[i].split(' ')
        E = int(line[1][:2]) * 60 * 60 * 1000
        E += int(line[1][3:5]) * 60 * 1000
        E += int((float(line[1][6:]) * 1000))
        S = E - int(''.join(line[2][:-1].split('.')).ljust(4,'0')) + 1
        lines[i] = [S,E]

    lines.sort(key=lambda x:(x[1], x[0]))
    for i in range(len(lines)):
        cnt = 1
        end = lines[i][1] + 1000
        for j in range(i + 1, len(lines)):
            start = lines[j][0]
            if start < end:
                cnt += 1
        answer = max(answer, cnt)
    return answer

lines = ["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]
print(solution(lines))  #1

lines = ["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]
print(solution(lines))  #2

lines = ["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s","2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s","2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s","2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s","2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]
print(solution(lines))  #7