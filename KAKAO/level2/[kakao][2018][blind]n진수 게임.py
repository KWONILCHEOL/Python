# [kakao][2018][blind]n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    game = "0"
    for i in range(t*m):
        j = i
        temp = ""
        while j:
            div = str(j%n)
            if int(div) > 9:
                div = chr(ord('A') + int(div) - 10)
            temp = div + temp
            j //= n
        game += temp

    answer = game[p-1::m][:t]
    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))