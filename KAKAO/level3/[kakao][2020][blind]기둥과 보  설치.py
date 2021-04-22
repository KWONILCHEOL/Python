# [kakao][2020][blind]기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

def check(answer):
    for x,y,a in answer:
        if a == 0:
            if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False
        elif a == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                continue
            if [x-1,y,1] in answer and [x+1,y,1] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for x,y,a,b in build_frame: #a0(기둥) a1(보)
        if b == 0:  # 삭제
            answer.remove([x,y,a])
            if not check(answer):
                answer.append([x,y,a])
        elif b == 1: # 추가
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x,y,a])
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame)) #[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame)) #[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]