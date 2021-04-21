# [kakao][2018][blind]압축
# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(ord('A')+ i)] = i + 1
    end = 27
    i = 0
    while i < len(msg):
        j = i + 1
        for j in range(i+ 1, len(msg) + 1):
            if msg[i:j] not in dic.keys():
                j -= 1
                break

        answer.append(dic[msg[i:j]])
        dic[msg[i:j+1]] = end
        end += 1
        i = j

    return answer

print(solution("KAKAO"))  # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT"))  # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB"))  # [1, 2, 27, 29, 28, 31, 30]