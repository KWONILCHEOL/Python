# [kakao][2018][blind]뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    for s in board : s.reverse()
    while True:
        temp = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if len(board[i]) > j + 1:
                    if len(board[i+1]) > j + 1:
                        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                            temp.add((i, j))
                            temp.add((i+1, j))
                            temp.add((i, j+1))
                            temp.add((i+1, j+1))
        if len(temp) == 0:
            break

        temp = sorted(list(temp), key=lambda x : x[1], reverse=True)
        answer += len(temp)
        for i,j in temp:
            board[i] = board[i][:j] + board[i][j+1:]
    return answer

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))  # 14

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,board))  #15