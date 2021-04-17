# [kakao][2019][blind]실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        fail = 0 if length == 0 else (count / length)
        answer.append((i, fail))
        length -= count

    answer.sort(key=lambda x:x[1],reverse=True)
    answer = [i[0] for i in answer]

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))  #[3,4,2,1,5]

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))  #[4,1,2,3]