# [kakao][2019][intern]크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    board = list(map(list, zip(*board)))

    for x in board:
        while 0 in x:
            x.remove(0)

    basket = []
    for i in moves:
        i -= 1
        if board[i]:
            if basket and basket[-1] == board[i][0]:
                answer += 2
                basket.pop()
            else:
                basket.append(board[i][0])
            board[i].remove(board[i][0])

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))