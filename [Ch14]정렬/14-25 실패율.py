def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        fail = 0 if length == 0 else (count / length)
        answer.extend([i, fail)])
        length -= count
    
    answer.sort(key = lambda x : x[1], reverse = True)
    answer = [i[0] for i in answer]
    
    return answer