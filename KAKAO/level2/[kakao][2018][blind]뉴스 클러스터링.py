# [kakao][2018][blind]뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

def step(w):
    if w == "":
        return ""

    cnt = 0
    u, v = "", ""
    correct = True
    for i in range(len(w)):
        if w[i] == '(': cnt += 1
        else: cnt -= 1

        if cnt < 0: correct = False
        if cnt == 0:
            u = w[:i+1]
            v = w[i+1:]
            break

    if correct:
        return u + step(v)
    else:
        u = u[1:-1].replace('(','a').replace(')','(').replace('a',')')
        temp = '(' + step(v) + ')' + u
        return temp

def solution(p):
    answer = step(p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))