from bisect import bisect_left
changes = []

def make_cases():
    global changes
    for x in range(16):
        changes.append(bin(x)[2:].zfill(4))

# 1을 가리키는 인덱스에 해당하는 속성 값을 '-'으로 바꿔준다.
def replace(change, data):
    for i in range(4):
        if change[i] == '1' : data[i] = '-'

    return data

def copy(data):
    _data = []
    for item in data: _data.append(item)

    return _data

def search(scores, num):
    return len(scores) - bisect_left(scores, num)

def solution(info, query):
    global changes
    answer = []
    info_dict = {}
    make_cases()

    # query를 위한 info 전처리
    for data in info:
        data = data.split()
        score = int(data[-1])
        data = data[:4]

        for change in changes:
            _data = copy(data)
            _data = replace(change, _data)
            _data = ''.join(_data)

            if _data not in info_dict.keys():
                info_dict[_data] = [score]
            else:
                info_dict[_data].append(score)

    # info_dict[key] 정렬
    for key in info_dict.keys(): info_dict[key].sort()

    for q in query:
        q = q.replace('and ','').split(' ')
        score = int(q[-1])
        q = ''.join(q[:-1])

        # 문의 조건을 만족하는 지원서들의 수 찾기
        cnt = 0
        if q in info_dict.keys():
            cnt = search(info_dict[q], score)

        answer.append(cnt)

    return answer