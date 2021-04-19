# [kakao][2019][blind]후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

def solution(relation):
    answer = []
    r, c = len(relation), len(relation[0])
    for b in range(1, 1 << c):
        tmp_set = set()
        for j in range(r):
            tmp = ''
            for k in range(c):
                if b & (1 << k):
                    tmp += relation[j][k]
            tmp_set.add(tmp)

        if len(tmp_set) == r:
            not_duplicate = True
            for num in answer:
                if (num & b) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer.append(b)
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))   #2