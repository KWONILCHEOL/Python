# [kakao][2018][blind]캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    if cacheSize == 0:
        return len(cities) * 5

    que = deque()
    for city in cities:
        if city in que:
            answer += 1
            que.remove(city)
            que.append(city)
        else:
            answer += 5
            if len(que) == cacheSize:
                que.popleft()
            que.append(city)
    return answer

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# print(solution(cacheSize, cities))  #50
#
# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
# print(solution(cacheSize, cities))  #21
#
# cacheSize = 2
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# print(solution(cacheSize, cities))  #60
#
# cacheSize = 5
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# print(solution(cacheSize, cities))  #52

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))  #16

# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# print(solution(cacheSize, cities))  #25