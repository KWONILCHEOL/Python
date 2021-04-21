# [programmers]숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

from collections import deque
def solution(n):
    answer = 1
    x = deque()
    for i in range(1,n//2 + 2): #15 -> 7 + 2 -> 1부터 8까지
        x.append(i)
        while True:
            _sum = sum(x)
            if _sum == n:
                answer += 1
                break
            elif _sum > n:
                x.popleft()
            elif _sum < n:
                break

    return answer

print(solution(15))