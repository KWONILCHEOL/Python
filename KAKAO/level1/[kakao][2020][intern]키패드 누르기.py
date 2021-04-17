# [kakao][2020][intern]키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    L = (4,1)
    R = (4,3)
    for x in numbers:
        if x == 0:
            x = 11
        if x % 3 == 1:
            answer += 'L'
            L = (x // 3 + 1, 1)
        elif x % 3 == 0:
            answer += 'R'
            R = (x // 3, 3)
        else:
            x, y = x // 3 + 1, x % 3
            Ld = abs(L[0] - x) + abs(L[1] - y)
            Rd = abs(R[0] - x) + abs(R[1] - y)
            if Ld < Rd:
                answer += 'L'
                L = (x,y)
            elif Ld > Rd:
                answer += 'R'
                R = (x, y)
            else:
                if hand == "right":
                    answer += 'R'
                    R = (x, y)
                else:
                    answer += 'L'
                    L = (x, y)

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))  #LRLLLRLLRRL

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))  #LRLLRRLLLRR

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))  #LLRLLRLLRL
