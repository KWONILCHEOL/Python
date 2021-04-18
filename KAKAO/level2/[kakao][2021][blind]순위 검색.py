# [kakao][2021][blind]순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left
def solution(info, query):
    answer = []
    dic = {}

    for x in info:
        temp = x.split(' ')
        key = ''.join(temp[:-1])
        value = int(temp[-1])
        if key in dic.keys():
            dic[key].append(value)
        else:
            dic[key] = [value]

    for key in dic.keys():
        if len(dic[key]) > 1:
            dic[key].sort()

    for q in query:
        q = q.replace('and ','').split(' ')

        if q[0] != '-': q[0] = [q[0]]
        else: q[0] = ["cpp","java","python"]

        if q[1] != '-': q[1] = [q[1]]
        else: q[1] = ["backend", "frontend"]

        if q[2] != '-': q[2] = [q[2]]
        else: q[2] = ["junior", "senior"]

        if q[3] != '-': q[3] = [q[3]]
        else: q[3] = ["chicken", "pizza"]

        cnt = 0
        for a in q[0]:
            for b in q[1]:
                for c in q[2]:
                    for d in q[3]:
                        if a+b+c+d in dic.keys():
                            idx = bisect_left(dic[a+b+c+d],int(q[4]))
                            cnt += len(dic[a+b+c+d]) - idx
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query)) #[1,1,1,1,2,4]


# from bisect import bisect_left
# changes = []
#
# def make_cases():
#     global changes
#     for x in range(16):
#         changes.append(bin(x)[2:].zfill(4))
#     print(changes)
# def replace(change, data):
#     for i in range(4):
#         if change[i] == '1' : data[i] = '-'
#
#     return data
#
# def copy(data):
#     _data = []
#     for item in data: _data.append(item)
#
#     return _data
#
# def search(scores, num):
#     return len(scores) - bisect_left(scores, num)
#
# def solution(info, query):
#     global changes
#     answer = []
#     info_dict = {}
#     make_cases()
#
#     for data in info:
#         data = data.split()
#         score = int(data[-1])
#         data = data[:4]
#
#         for change in changes:
#             _data = copy(data)
#             _data = replace(change, _data)
#             _data = ''.join(_data)
#
#             if _data not in info_dict.keys():
#                 info_dict[_data] = [score]
#             else:
#                 info_dict[_data].append(score)
#
#     # info_dict[key] 정렬
#     for key in info_dict.keys(): info_dict[key].sort()
#
#     for q in query:
#         q = q.replace('and ','').split(' ')
#         score = int(q[-1])
#         q = ''.join(q[:-1])
#
#         cnt = 0
#         if q in info_dict.keys():
#             cnt = search(info_dict[q], score)
#
#         answer.append(cnt)
#
#     return answer
#
# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# print(solution(info, query)) #[1,1,1,1,2,4]