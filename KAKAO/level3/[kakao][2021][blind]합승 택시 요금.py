# [kakao][2021][blind]합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

INF = int(1e9)
def solution(n, s, a, b, fares):
    G = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        G[i][i] = 0

    for x, y, d in fares:
        G[x][y] = d
        G[y][x] = d

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                cost = G[i][k] + G[k][j]
                if cost < G[i][j]:
                    G[i][j] = cost

    answer = min([G[s][i] + G[i][a] + G[i][b] for i in range(1, n+1)])
    return answer

n,s,a,b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n,s,a,b,fares))

# n,s,a,b = 7,3,4,1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# print(solution(n,s,a,b,fares))
#
# n,s,a,b = 6,4,5,6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# print(solution(n,s,a,b,fares))