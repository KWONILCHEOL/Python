# [kakao][2018][blind]오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = dict()
    for data in record:
        temp = data.split(' ')
        state = temp[0]
        id = temp[1]
        if state == 'Leave':
            answer.append([id,"님이 나갔습니다."])
        else:
            if state == 'Enter':
                answer.append([id,"님이 들어왔습니다."])
            dic[id] = temp[2]

    for i in range(len(answer)):
        answer[i] = dic[answer[i][0]] + answer[i][1]

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))